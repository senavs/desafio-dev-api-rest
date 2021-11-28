from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


async def handler_python_exceptions(_: Request, __: Exception) -> JSONResponse:
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})


async def handler_http_request(_: Request, exception: HTTPException) -> JSONResponse:
    return JSONResponse(status_code=exception.status_code, content={"message": str(exception.detail)})


async def handler_request_validation(_: Request, exception: RequestValidationError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": str(exception)})


exception_handlers = {
    Exception: handler_python_exceptions,
    HTTPException: handler_http_request,
    RequestValidationError: handler_request_validation,
}
