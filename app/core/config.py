from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Config(BaseSettings):
    
    allowed_origins: list[str] = Field(default=["http://localhost:3000"],alias="ALLOWED_ORIGINS")
    supabase_url: str = Field(default="", alias="SUPABASE_URL")
    supabase_key: str = Field(default="", alias="SUPABASE_KEY")
    supabase_schema: str = Field(default="public", alias="SUPABASE_SCHEMA")
    table_products: str = Field(default="products", alias="TABLE_PRODUCTS")

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore"
    )



config = Config()
#print(config.prueba1)
#print(config.prueba2)