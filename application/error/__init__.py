from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


class ApplicationException(HTTPException):
    """Base application exception"""

    status_code: int

    def __init__(self, custom_message: str = None):
        super().__init__(self.status_code, self.__class__.__doc__ or custom_message or "")


class BadRequestException(ApplicationException):
    """HTTP base exception for bad request"""

    status_code = HTTP_400_BAD_REQUEST


class NotFoundException(ApplicationException):
    """HTTP base exception for not found"""

    status_code = HTTP_404_NOT_FOUND
