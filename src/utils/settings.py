from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file = ".env", extra = "ignore")   #helps to tell where is the the data coming from from which file it is coming

    DB_CONNECTION: str
    SECRET_KEY: str
    ALGORITHM: str
    EXP_TIME: int

settings = Settings()  #whenever there is the requirement of db_connection we can import settings for it 

#print(settings.DB_CONNECTION)