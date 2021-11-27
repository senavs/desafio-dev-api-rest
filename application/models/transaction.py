from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field
from sqlalchemy import DATETIME, DECIMAL, INTEGER, Column, ForeignKey, func
from sqlalchemy.orm import backref, relationship

from ..database.session import DeclarativeBase
from ._base import TableBaseModel


class TransactionTable(DeclarativeBase, TableBaseModel):
    __tablename__ = "TRANSACAO"
    __table_args__ = {"extend_existing": True}

    ID_TRANSACAO = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    ID_CONTA = Column(INTEGER, ForeignKey("CONTA.ID_CONTA", ondelete="CASCADE"), nullable=False)
    VALOR = Column(DECIMAL(2), nullable=False)
    DATA_CRIACAO = Column(DATETIME, nullable=False, default=func.now(), server_default=func.now())

    account = relationship(
        "AccountTable", backref=backref("transactions", cascade="all,delete", lazy="dynamic")
    )


class TransactionModel(BaseModel):
    id_transacao: int = Field(alias="ID_TRANSACAO")
    id_conta: int = Field(alias="ID_CONTA")
    valor: Decimal = Field(alias="VALOR")
    data_criacao: datetime = Field(alias="DATA_CRIACAO")
