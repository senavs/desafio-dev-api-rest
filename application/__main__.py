import uvicorn

from . import settings
from .app import create_app

if __name__ == "__main__":
    app = create_app()

    uvicorn.run(
        "__main__:app",
        host=settings.deploy.HOST,
        port=settings.deploy.PORT,
        debug=settings.deploy.DEBUG,
    )
