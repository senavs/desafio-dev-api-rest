from fastapi import FastAPI

from . import __version__, settings
from .middlewares.handlers import exception_handlers


def create_app():
    app = FastAPI(
        title=settings.application.TITLE,
        description=settings.application.DESCRIPTION,
        version=__version__,
        exception_handlers=exception_handlers,
    )

    return app
