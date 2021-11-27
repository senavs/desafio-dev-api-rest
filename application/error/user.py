from . import BadRequestException, NotFoundException


class UserNotFoundException(NotFoundException):
    """user not found"""


class UserAlreadyRegisteredException(BadRequestException):
    """user already registered"""
