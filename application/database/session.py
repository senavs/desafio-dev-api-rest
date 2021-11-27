from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base, sessionmaker

from application import settings

engine = create_engine(settings.database.DATABASE_URI)
DeclarativeBase: DeclarativeMeta = declarative_base()
Session: sessionmaker = sessionmaker(engine)

from ..models.user import UserTable  # noqa: F401, E402
