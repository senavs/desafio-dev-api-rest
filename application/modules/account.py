from ..database.client import DatabaseClient
from ..error.account import InvalidAccountTypeException
from ..models.account import AccountModel, AccountTable
from ..models.account_type import AccountTypeTable
from .user import search_user


def create_account(id_user: int, id_account_type: int) -> AccountModel:
    """Crate new user account"""

    with DatabaseClient() as conn:
        search_user(id_user)  # search if user exists or raises 404

        if not conn.query(AccountTypeTable).get(id_account_type):
            raise InvalidAccountTypeException

        account = AccountTable(ID_PESSOA=id_user, ID_TIPO_CONTA=id_account_type)
        account.insert(conn)

        account_model = AccountModel.from_orm(account)
    return account_model
