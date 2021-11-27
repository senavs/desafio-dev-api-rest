from datetime import datetime

from fastapi import HTTPException

from ..database.client import DatabaseClient
from ..models.user import UserModel, UserTable


def search_user(id: int = None) -> UserModel:
    """Search for a user"""

    with DatabaseClient() as conn:
        user = conn.session.query(UserTable).get(id)
        if not user:
            raise HTTPException(404, "user not found")

        user_model = UserModel.from_orm(user)
    return user_model


def create_user(name: str, cpf: str, birthday: datetime) -> UserModel:
    """Insert new user into database"""

    with DatabaseClient() as conn:
        if conn.session.query(UserTable).filter(UserTable.CPF == cpf).first():
            raise HTTPException(400, "user already registered")

        user = UserTable(NOME=name, CPF=cpf, DATA_NASCIMENTO=birthday)
        user.insert(conn)

        user_model = UserModel.from_orm(user)
    return user_model
