from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


class ApplicationException(HTTPException):
    """Base application exception"""

    status_code: int

    def __init__(self):
        super().__init__(self.status_code, self.detail)

    @property
    def detail(self) -> str:
        """Class doc string is the error detail"""

        return self.__class__.__doc__ or ""


class BadRequestException(ApplicationException):
    """HTTP base exception for bad request"""

    status_code = HTTP_400_BAD_REQUEST


class NotFoundException(ApplicationException):
    """HTTP base exception for not found"""

    status_code = HTTP_404_NOT_FOUND
