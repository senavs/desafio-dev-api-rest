from .session import DeclarativeBase, engine


class Bootloader:
    @classmethod
    def create(cls):
        DeclarativeBase.metadata.create_all(engine)

    @classmethod
    def reset(cls):
        DeclarativeBase.metadata.drop_all(engine)
