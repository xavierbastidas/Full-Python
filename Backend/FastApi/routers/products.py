from fastapi import APIRouter
router = APIRouter(prefix="/api/v2/products",
                   tags= ["products"],
                   responses={404:{"message":"Not found"}})

products_list= ["Product 1","Product 2",
                "Product 3","Product 4","Product 5"]

@router.get("/")
async def produts():
    return products_list

@router.get("/{id}")
async def produts(id:int):
    return products_list[id]


