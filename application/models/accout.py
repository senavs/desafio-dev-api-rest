from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field
from sqlalchemy import BOOLEAN, DATETIME, DECIMAL, INTEGER, Column, ForeignKey, func
from sqlalchemy.orm import backref, relationship

from ..database.session import DeclarativeBase
from ._base import TableBaseModel


class AccountTable(DeclarativeBase, TableBaseModel):
    __tablename__ = "CONTA"
    __table_args__ = {"extend_existing": True}

    ID_CONTA = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    ID_PESSOA = Column(INTEGER, ForeignKey("PESSOA.ID_PESSOA", ondelete="CASCADE"), nullable=False)
    SALDO = Column(DECIMAL(2), nullable=False, default="0", server_default="0")
    ATIVO = Column(BOOLEAN, nullable=False, default=True)
    ID_TIPO_CONTA = Column(
        INTEGER, ForeignKey("TIPO_CONTA.ID_TIPO_CONTA", ondelete="CASCADE"), nullable=False
    )
    DATA_CRIACAO = Column(DATETIME, nullable=False, default=func.now(), server_default=func.now())

    user = relationship("UserTable", backref=backref("accounts", cascade="all,delete", lazy="dynamic"))
    type = relationship("AccountTypeTable", backref=backref("accounts", cascade="all,delete", lazy="dynamic"))


class AccountModel(BaseModel):
    id_conta: int = Field(alias="ID_CONTA")
    id_pessoa: int = Field(alias="ID_PESSOA")
    saldo: Decimal = Field(alias="SALDO")
    ativo: bool = Field(alias="ATIVO")
    id_tipo_conta: int = Field(alias="ID_TIPO_CONTA")
    data_criacao: datetime = Field(alias="DATA_CRIACAO")
