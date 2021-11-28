from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel


class Payload(BaseModel):
    class Config:
        json_encoders: dict = {datetime: lambda x: x.isoformat(), date: lambda x: x.isoformat(), Decimal: str}
        allow_population_by_field_name: bool = True
