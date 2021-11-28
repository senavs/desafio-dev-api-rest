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
    SALDO = Column(DECIMAL(2), nullable=False, default="0")
    LIMITE_SAQUE_DIARIO = Column(DECIMAL(2), nullable=False, default="0")
    ATIVO = Column(BOOLEAN, nullable=False, default=True)
    ID_TIPO_CONTA = Column(
        INTEGER, ForeignKey("TIPO_CONTA.ID_TIPO_CONTA", ondelete="CASCADE"), nullable=False
    )
    DATA_CRIACAO = Column(DATETIME, nullable=False, default=func.now(), server_default=func.now())

    user = relationship("UserTable", backref=backref("accounts", cascade="all,delete", lazy="dynamic"))
    type = relationship("AccountTypeTable", backref=backref("accounts", cascade="all,delete", lazy="dynamic"))


class AccountModel(BaseModel):
    id_account: int = Field(alias="ID_CONTA")
    id_user: int = Field(alias="ID_PESSOA")
    amount: Decimal = Field(alias="SALDO")
    limit: Decimal = Field(alias="LIMITE_SAQUE_DIARIO")
    active: bool = Field(alias="ATIVO")
    id_account_type: int = Field(alias="ID_TIPO_CONTA")
    create_at: datetime = Field(alias="DATA_CRIACAO")

    class Config:
        orm_mode = True
