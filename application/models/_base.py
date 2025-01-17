from typing import Any, Optional

from ..database.client import DatabaseClient


class TableBaseModel:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def search(cls, connection: DatabaseClient, id: int) -> "TableBaseModel":
        return connection.query(cls).get(id)

    def insert(self, connection: DatabaseClient, *, flush: bool = False, commit: bool = True):
        connection.add(self)
        if flush:
            connection.flush()
        if commit:
            connection.commit()

    def update(self, connection: DatabaseClient, *, flush: bool = False, commit: bool = True, **data: Any):
        for attr, new_value in data.items():
            if not hasattr(self, attr):
                raise ValueError(f"{self.__class__.__name__} as no attribute {attr} to update")
            if new_value is not None:
                setattr(self, attr, new_value)
        if flush:
            connection.flush()
        if commit:
            connection.commit()

    def delete(self, connection: DatabaseClient, *, flush: bool = False, commit: bool = True):
        connection.session.delete(self)
        if flush:
            connection.flush()
        if commit:
            connection.commit()

    def to_dict(self, *, exclude: Optional[list] = None, **include) -> dict:
        if not exclude:
            exclude = []

        attrs = {
            attr.lower(): getattr(self, attr)
            for attr in self.__dir__()
            if attr.isupper() and attr not in exclude
        }
        attrs.update(**include)
        return attrs

    def __repr__(self):
        return f"{type(self).__qualname__}({self.to_dict()})"
