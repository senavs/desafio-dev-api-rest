from datetime import date

from fastapi import APIRouter

from application.modules.transaction import OperationEnum, operation, report, transaction
from application.routes.payloads.transaction import (
    ListTransactionResponse,
    OperationRequest,
    OperationResponse,
    TransactionRequest,
    TransactionResponse,
)

router = APIRouter(prefix="/account/operation", tags=["Account Operations"])


@router.get("/{id}", summary="List operations", response_model=ListTransactionResponse)
def _report(id: int, from_date: date, to_date: date) -> ListTransactionResponse:
    ops = report(id, from_date, to_date)
    return ListTransactionResponse(operations=ops)


@router.post("/deposit", summary="Deposit (add value)", response_model=OperationResponse)
def _deposit(body: OperationRequest) -> OperationResponse:
    op = operation(**body.dict(), operation_type=OperationEnum.deposit)
    return OperationResponse(**op.dict())


@router.post("/withdraw", summary="Withdraw (remove value)", response_model=OperationResponse)
def _withdraw(body: OperationRequest) -> OperationResponse:
    op = operation(**body.dict(), operation_type=OperationEnum.withdraw)
    return OperationResponse(**op.dict())


@router.post("/transaction", summary="Withdraw (remove value)", response_model=TransactionResponse)
def _transaction(body: TransactionRequest) -> TransactionResponse:
    ops = transaction(**body.dict())
    return TransactionResponse(operations=ops)
