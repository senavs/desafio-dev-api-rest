from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from application.routes.payloads import Payload


class BaseAccountPayload(Payload):
    id_user: int = Field(alias="idUsuario")
    amount: Decimal = Field(alias="saldo")
    active: bool = Field(alias="ativo")
    id_account_type: int = Field(alias="idTipoConta")
    create_at: datetime = Field(alias="dataCriacao")


class AccountPayload(BaseAccountPayload):
    id_account: int = Field(alias="idConta")


class CreateAccountRequest(BaseModel):
    """Request model to endpoint POST /accounts/"""

    id_user: int = Field(alias="idUsuario")
    id_account_type: int = Field(alias="idTipoConta")


class CreateAccountResponse(AccountPayload):
    """Response model to endpoint POST /accounts/"""
