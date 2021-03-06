from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = 'mysql+pymysql://root:@localhost:3306/crudfastapi'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
