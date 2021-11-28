from decimal import Decimal

from ..database.client import DatabaseClient
from ..error.account import (
    AccountNotFoundException,
    InvalidAccountLimitException,
    InvalidAccountTypeException,
)
from ..models.account import AccountModel, AccountTable
from ..models.account_type import AccountTypeTable
from .user import search_user


def search_account(id_account: int, *, connection: DatabaseClient = None) -> AccountModel:
    """Search for user account"""

    with DatabaseClient(connection=connection) as conn:
        account = conn.query(AccountTable).get(id_account)
        if not account:
            raise AccountNotFoundException

        account_model = AccountModel.from_orm(account)
    return account_model


def list_user_accounts(id_user: int) -> list[AccountModel]:
    """Search for user account"""

    with DatabaseClient() as conn:
        search_user(id_user, connection=conn)  # search if user exists or raises 404

        accounts = conn.query(AccountTable).filter(AccountTable.ID_PESSOA == id_user).all()

        accounts_model = [AccountModel.from_orm(account) for account in accounts]
    return accounts_model


def create_account(id_user: int, limit: Decimal, id_account_type: int) -> AccountModel:
    """Crate new user account"""

    with DatabaseClient() as conn:
        search_user(id_user, connection=conn)  # search if user exists or raises 404

        if not conn.query(AccountTypeTable).get(id_account_type):
            raise InvalidAccountTypeException

        if limit <= 0:
            raise InvalidAccountLimitException

        account = AccountTable(ID_PESSOA=id_user, LIMITE_SAQUE_DIARIO=limit, ID_TIPO_CONTA=id_account_type)
        account.insert(conn)

        account_model = AccountModel.from_orm(account)
    return account_model


def update_account_limit(id_account: int, limit: Decimal) -> bool:
    """Update account limit"""

    with DatabaseClient() as conn:
        search_account(id_account, connection=conn)  # search if account exists or raises 404

        if limit <= 0:
            raise InvalidAccountLimitException

        was_update = (
            conn.query(AccountTable)
            .filter(AccountTable.ID_CONTA == id_account)
            .update({"LIMITE_SAQUE_DIARIO": limit})
        )
        conn.commit()

    return was_update


def update_account_status(id_account: int, active: bool) -> bool:
    """Update account status (activate or deactivate)"""

    with DatabaseClient() as conn:
        search_account(id_account, connection=conn)  # search if account exists or raises 404

        was_update = (
            conn.query(AccountTable).filter(AccountTable.ID_CONTA == id_account).update({"ATIVO": active})
        )
        conn.commit()

    return was_update
