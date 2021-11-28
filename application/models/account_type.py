from pydantic import BaseModel, Field
from sqlalchemy import INTEGER, VARCHAR, Column

from ..database.session import DeclarativeBase
from ._base import TableBaseModel


class AccountTypeTable(DeclarativeBase, TableBaseModel):
    __tablename__ = "TIPO_CONTA"
    __table_args__ = {"extend_existing": True}

    ID_TIPO_CONTA = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    NOME = Column(VARCHAR(32), nullable=False)
    DESCRICAO = Column(VARCHAR(32))


class AccountTypeModel(BaseModel):
    id_tipo_conta: int = Field(alias="ID_TIPO_CONTA")
    nome: str = Field(alias="NOME")
    descricao: str = Field(alias="DESCRICAO")
