from fastapi import APIRouter

from ..modules.user import create_user, search_user
from ..routes.payloads.user import CreateUserRequest, CreateUserResponse, SearchUserResponse

router = APIRouter(prefix="/users", tags=["User"])


@router.get("/{id}", summary="Search for a user", response_model=SearchUserResponse)
def _search_user(id: int) -> SearchUserResponse:
    user = search_user(id)
    return SearchUserResponse(**user.dict())


@router.post("/", summary="Create user", response_model=CreateUserResponse)
def _create_user(body: CreateUserRequest) -> CreateUserResponse:
    user = create_user(**body.dict())
    return CreateUserResponse(**user.dict())
