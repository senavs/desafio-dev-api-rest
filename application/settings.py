from pydantic import BaseSettings
from pydantic.fields import Undefined


class SettingsAddsOn:
    def __getattr__(self, name: str):
        """Raise undefined settings during runtime instead of startup"""

        if issubclass(getattr(self, name, None), Undefined):
            raise RuntimeError(f"you are trying to access an undefined setting: {name}")
        super().__getattribute__(name)


class DeploySettings(BaseSettings, SettingsAddsOn):
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DEBUG: bool = True


class ApplicationSettings(BaseSettings, SettingsAddsOn):
    TITLE: str = "Translation API"
    DESCRIPTION: str = "DOCK Python API challenge"


class DatabaseSettings(BaseSettings, SettingsAddsOn):
    DATABASE_URI: str = "mysql+mysqlconnector://APPLICATION_USER:application-user-password@0.0.0.0:3306/DOCK"


deploy = DeploySettings()
application = ApplicationSettings()
database = DatabaseSettings()
