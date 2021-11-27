import uvicorn

from application import settings
from application.app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "application.__main__:app",
        host=settings.deploy.HOST,
        port=settings.deploy.PORT,
        debug=settings.deploy.DEBUG,
        reload=True,
    )
