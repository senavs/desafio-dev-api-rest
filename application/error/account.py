from . import BadRequestException, NotFoundException


class InvalidAccountTypeException(BadRequestException):
    """invalid account type id"""


class InvalidAccountLimitException(BadRequestException):
    """invalid account limit"""


class AccountNotFoundException(NotFoundException):
    """account not found"""
