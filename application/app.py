from fastapi import FastAPI

from . import __version__, settings
from .database.loader import Bootloader
from .middlewares.handlers import exception_handlers
from .routes import account, user


def create_app():
    app = FastAPI(
        title=settings.application.TITLE,
        description=settings.application.DESCRIPTION,
        version=__version__,
        exception_handlers=exception_handlers,
    )

    # initialize database ORMs
    Bootloader.create()

    # routes
    app.include_router(user.router)
    app.include_router(account.router)

    return app
