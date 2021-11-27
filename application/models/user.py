from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import CHAR, DATETIME, INTEGER, VARCHAR, Column

from ..database.session import DeclarativeBase
from ._base import TableBaseModel


class UserTable(DeclarativeBase, TableBaseModel):
    __tablename__ = "PESSOA"
    __table_args__ = {"extend_existing": True}

    ID_PESSOA = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    NOME = Column(VARCHAR(128), nullable=False)
    CPF = Column(CHAR(11), nullable=False)
    DATA_NASCIMENTO = Column(DATETIME, nullable=False)


class UserModel(BaseModel):
    id_pessoa: int = Field(alias="ID_PESSOA")
    nome: str = Field(alias="NOME")
    cpf: str = Field(alias="CPF")
    data_nascimento: datetime = Field(alias="DATA_NASCIMENTO")
