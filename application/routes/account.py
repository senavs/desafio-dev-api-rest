from fastapi import APIRouter

from ..modules.account import create_account
from .payloads.account import CreateAccountRequest, CreateAccountResponse

router = APIRouter(prefix="/accounts", tags=["Account"])


@router.post("/", summary="Create new user account")
def _create_account(body: CreateAccountRequest) -> CreateAccountResponse:
    account = create_account(**body.dict())
    return CreateAccountResponse(**account.dict())
