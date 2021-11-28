from . import BadRequestException


class AccountDeactivatedException(BadRequestException):
    """account is deactivated"""


class NoBalanceException(BadRequestException):
    """no enough balance"""


class NoMoreLimitException(BadRequestException):
    """account has no more limit"""


class TooMuchValueException(BadRequestException):
    """new value reaches the account daily limit"""
