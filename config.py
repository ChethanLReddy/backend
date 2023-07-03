from pydantic import BaseSettings


class Setting(BaseSettings):
    database_hostname: str = 'localhost'
    database_port: str = '5432'
    database_password: str = 'postgres'
    database_name: str = 'postgres'
    database_username: str = 'postgres'
    secrete_key: str = 'kjsbdkgjbrsgfvsdf7bvksd87fkshfdshgjhdfsfg'
    algorithm:  str = 'HS256'
    access_token_expiry_minutes: int = 2000

    # class Config:
        # env_file = '.env'


setting = Setting()