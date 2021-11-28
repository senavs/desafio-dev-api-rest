from fastapi import APIRouter

from ..modules.account import (
    create_account,
    list_user_accounts,
    search_account,
    update_account_limit,
    update_account_status,
)
from .payloads.account import (
    CreateAccountRequest,
    CreateAccountResponse,
    ListAccountResponse,
    SearchAccountResponse,
    UpdateAccountRequest,
)

router = APIRouter(prefix="/accounts", tags=["Account"])


@router.get("/{id}", summary="Search for account", response_model=SearchAccountResponse)
def _search_account(id: int) -> SearchAccountResponse:
    account = search_account(id)
    return SearchAccountResponse(**account.dict())


@router.post("/", summary="Create new user account", response_model=CreateAccountResponse)
def _create_account(body: CreateAccountRequest) -> CreateAccountResponse:
    account = create_account(**body.dict())
    return CreateAccountResponse(**account.dict())


@router.put("/{id}", summary="Update account limit", response_model=bool)
def _update_account(id: int, body: UpdateAccountRequest) -> bool:
    return update_account_limit(id, body.limit)


@router.delete("/{id}", summary="Deactivate account", response_model=bool)
def _deactivate_account(id: int) -> bool:
    return update_account_status(id, False)


@router.get("/user/{id}", summary="List all user accounts", response_model=ListAccountResponse)
def _list_accounts(id: int) -> ListAccountResponse:
    accounts = list_user_accounts(id)
    return ListAccountResponse(accounts=accounts)
