from datetime import date
from decimal import Decimal
from typing import Union

from pydantic import BaseModel, Field

from application.models.transaction import TransactionModel
from application.routes.payloads import Payload


class BaseTransactionPayload(Payload):
    id_account: int = Field(alias="idConta")
    value: Decimal = Field(alias="valor")
    create_at: date = Field(alias="dataCriacao")


class TransactionPayload(BaseTransactionPayload):
    id_transaction: int = Field(alias="idTransacao")


class OperationRequest(BaseModel):
    """Request model to endpoint POST /accounts/operations/{withdraw|deposit}"""

    id_account: int = Field(alias="idConta")
    value: Decimal = Field(alias="valor", gt=0)


class OperationResponse(TransactionPayload):
    """Response model to endpoint POST /accounts/operations/{withdraw|deposit}"""


class TransactionRequest(BaseModel):
    """Request model to endpoint POST /accounts/operations/transaction"""

    from_id_account: int = Field(alias="idContaOrigem")
    to_id_account: int = Field(alias="idContaDestino")
    value: Decimal = Field(alias="valor", gt=0)


class TransactionResponse(BaseModel):
    """Response model to endpoint POST /accounts/operations/transaction"""

    operations: tuple[Union[TransactionPayload, TransactionModel], ...]


class ListTransactionResponse(BaseModel):
    """Response model to endpoint GET /accounts/operations/"""

    operations: list[Union[TransactionPayload, TransactionModel]]
