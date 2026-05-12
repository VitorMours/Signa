from pydantic_settings import BaseSettings 
from dotenv import load_dotenv

class Config(BaseSettings):
    load_dotenv()
    API_KEY: str = ""
    API_KEY_NAME: str = ""
    API_KEY_HEADER: str = ""
    title: str = "Sonjis API"

    class Config:
      env_file = ".env"
      
config = Config()