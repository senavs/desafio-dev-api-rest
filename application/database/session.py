from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base, sessionmaker

from application import settings

engine = create_engine(settings.database.DATABASE_URI)
DeclarativeBase: DeclarativeMeta = declarative_base()
Session: sessionmaker = sessionmaker(engine)

from ..models.accout import AccountTable  # noqa: F401, E402
from ..models.accout_type import AccountTypeTable  # noqa: F401, E402
from ..models.transaction import TransactionTable  # noqa: F401, E402
from ..models.user import UserTable  # noqa: F401, E402
