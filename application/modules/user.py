from datetime import datetime

from ..database.client import DatabaseClient
from ..error.user import UserAlreadyRegisteredException, UserNotFoundException
from ..models.user import UserModel, UserTable


def search_user(id: int = None, *, connection: DatabaseClient = None) -> UserModel:
    """Search for a user"""

    with DatabaseClient(connection=connection) as conn:
        user = conn.query(UserTable).get(id)
        if not user:
            raise UserNotFoundException

        user_model = UserModel.from_orm(user)
    return user_model


def create_user(name: str, cpf: str, birthday: datetime) -> UserModel:
    """Insert new user into database"""

    with DatabaseClient() as conn:
        if conn.query(UserTable).filter(UserTable.CPF == cpf).first():
            raise UserAlreadyRegisteredException

        user = UserTable(NOME=name, CPF=cpf, DATA_NASCIMENTO=birthday)
        user.insert(conn)

        user_model = UserModel.from_orm(user)
    return user_model
