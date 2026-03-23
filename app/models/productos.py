from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from uuid import UUID

def validar_fecha_ingreso(value: date) -> date:
    if value > date.today():
        raise ValueError("La fecha de ingreso no puede ser futura")
    return value

class ProductCreate(BaseModel):
    name:str = Field(min_length = 1, max_length=200)
    quantity:int = Field(ge=0)
    ingreso_date: date 
    min_stock: int = Field(ge=0)
    max_stock: int = Field(ge=0)

    @field_validator("ingreso_date")
    @classmethod
    def validar_ingreso_date(cls, value:date) -> date:
        return validar_fecha_ingreso(value)

class ProductUpdate(BaseModel):
    name:str | None = Field(default=None, min_length =1, max_length = 200)
    quantity:int | None = Field(default=None, ge=0)
    ingreso_date: date
    min_stock: int | None = Field(default=None, ge=0)
    max_stock: int | None = Field(default=None, ge=0)
    @field_validator("ingreso_date")
    @classmethod
    def validar_ingreso_date(cls, value:date) -> date:
        return validar_fecha_ingreso(value)
    
class Product0out(BaseModel):
    id: UUID
    name: str
    quantity: int
    ingreso_date: date
    min_stock: int
    max_stock: int
    created_at: datetime
    updated_at: datetime

class ProductListOut(BaseModel):
    total: int
    items: list[Product0out]

