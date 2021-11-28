from datetime import date
from decimal import Decimal
from enum import Enum, auto

from sqlalchemy import DATE, cast, func

from ..database.client import DatabaseClient
from ..error.transaction import (
    AccountDeactivatedException,
    NoBalanceException,
    NoMoreLimitException,
    TooMuchValueException,
)
from ..models.account import AccountModel
from ..models.transaction import TransactionModel, TransactionTable
from .account import search_account, update_account_balance


class OperationEnum(Enum):
    deposit = auto()
    withdraw = auto()


def validate_limit(
    id_account: int,
    account_limit: Decimal,
    inc_value: Decimal = Decimal("0"),
    *,
    connection: DatabaseClient = None
):
    """Validate if account reached daily limit"""

    with DatabaseClient(connection=connection) as conn:
        total_withdraw_today = (
            conn.query(func.sum(TransactionTable.VALOR)).filter(
                TransactionTable.ID_CONTA == id_account,
                cast(TransactionTable.DATA_CRIACAO, DATE) >= date.today(),
                TransactionTable.VALOR < 0,
            )
        ).first()

        total_withdraw_today = abs(total_withdraw_today[0] or 0)

        if total_withdraw_today > account_limit:
            raise NoMoreLimitException

        if total_withdraw_today + inc_value > account_limit:
            raise TooMuchValueException


def validate_account(account: AccountModel, new_value: Decimal = None):
    """Validate account"""

    if not account.active:
        raise AccountDeactivatedException
    if new_value and new_value > account.amount:
        raise NoBalanceException


def operation(
    id_account: int, value: Decimal, operation_type: OperationEnum, *, connection: DatabaseClient = None
) -> TransactionModel:
    """Withdraw or Deposit value"""

    with DatabaseClient(connection=connection) as conn:
        account = search_account(id_account, connection=conn)  # search if account exists or raises 404

        if operation_type == OperationEnum.withdraw:
            validate_account(account, value)
            validate_limit(id_account, account.limit, value, connection=conn)

            value = -value
        else:
            validate_account(account)

        new_balance = account.amount + value

        transaction = TransactionTable(ID_CONTA=id_account, VALOR=value)
        transaction.insert(conn)

        update_account_balance(id_account, new_balance, connection=conn)

        transaction_model = TransactionModel.from_orm(transaction)
    return transaction_model


def transaction(from_id_account: int, to_id_account: int, value: Decimal) -> tuple[TransactionModel, ...]:
    """Move value to another account"""

    with DatabaseClient() as conn:
        search_account(from_id_account, connection=conn)  # search if account exists or raises 404
        search_account(to_id_account, connection=conn)  # search if account exists or raises 404

        cashout = operation(from_id_account, value, OperationEnum.withdraw, connection=conn)
        cashin = operation(to_id_account, value, OperationEnum.deposit, connection=conn)

    return cashout, cashin


def report(id_account: int, start_date: date, end_date: date) -> list[TransactionModel]:
    """List all account's operations"""

    with DatabaseClient() as conn:
        search_account(id_account, connection=conn)  # search if account exists or raises 404

        transactions = (
            conn.query(TransactionTable)
            .filter(
                TransactionTable.ID_CONTA == id_account,
                cast(TransactionTable.DATA_CRIACAO, DATE) >= start_date,
                cast(TransactionTable.DATA_CRIACAO, DATE) <= end_date,
            )
            .all()
        )

        transactions_model = [TransactionModel.from_orm(transaction) for transaction in transactions]
    return transactions_model
