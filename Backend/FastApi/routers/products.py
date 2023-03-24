from fastapi import APIRouter
router = APIRouter(prefix="/api/v2/products",
                   tags= ["products"],
                   responses={404:{"message":"No encontrado"}})

products_list= ["Producto 1","Producto 2",
                "Producto 3","Producto 4","Producto 5"]

@router.get("/")
async def produts():
    return products_list

@router.get("/{id}")
async def produts(id:int):
    return products_list[id]


