from uuid import UUID
from datetime import datetime, timezone
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from postgrest import CountMethod

def _table():
    sb = get_supabase()
    return sb.table(config.supabase_schema).table(config.table_products)

def list_products(limit: int = 100, offset: int = 0):
    try:
        res = _table().select("*", count = CountMethod.EXACT).range(offset, offset+limit-1).execute()
        return {"items": res.data or [], "total": res.count or 0}
    except Exception as e:
        raise HTTPException(status_code = 404, detail = "Producto no encontrado")

def get_product(product_id: UUID):
    try: 
        res =_table().select("*").eq("id", str(product_id)).single().execute()
        data = res.data or []
        return data[0]
    except Exception as e:
        raise HTTPException(status_code = 404, detail = "Producto no encontrado")

def create_product(datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code = 400, detail = "No enviaste campos para registrar")
        datos = jsonable_encoder(datos)
        res = _table().insert(datos).execute()
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Falló al insertar el registro {str(e)}")
    

def update_product(product_id: UUID, datos: dict):
    try:
        if not datos:
            raise HTTPException(status_code = 400, detail = "No enviaste campos para registrar")
        datos = jsonable_encoder(datos)
        res = _table().update(datos).eq("id", str(product_id)).execute()
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code = 404, detail = "Producto no encontrado")

def delete_product(product_id: UUID):
    try:
        res = _table().delete().eq("id", str(product_id)).execute()
        return res.data[0] if res.data else None
    except Exception as e:
        raise HTTPException(status_code = 404, detail = "Producto no encontrado")
    
