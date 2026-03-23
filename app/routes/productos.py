from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.models.productos import ProductCreate, ProductUpdate, Product0out, ProductListOut
from app.services.productos_service import list_products, get_product, create_product, update_product, delete_product

router = APIRouter(prefix="/products")

@router.get("/", response_model=ProductListOut, name="Listar_productos")
def inicio(
    limit: int = Query(100, ge = 1, le = 200), #Cuantos registros se van a mostrar
    offset: int = Query(0, ge = 0) #desde que registro se va a mostrar
):
    return list_products(limit, offset)

@router.get("/{product_id}", response_model = Product0out, name="Obtener_producto")
def obtener_producto(product_id: UUID):
    return get_product(product_id)

@router.post("/", response_model = Product0out, name="Crear_producto")
def crear_producto(body: ProductCreate):
    return create_product(body.model_dump())

@router.put("/{product_id}", response_model=Product0out, name="Actualizar_producto")
def update_producto(product_id: UUID, body: ProductUpdate):
    return update_product(product_id, body.model_dump())

@router.delete("/{product_id}", name="Eliminar_producto")
def eliminar_producto(product_id: UUID):
    return delete_product(product_id)