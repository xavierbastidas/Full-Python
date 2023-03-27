from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
router = APIRouter()

#Inicia el servidor : uvicorn users:app --reload
#Entidad user

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list= [User(id=1,name="xavier",surname="bastidas",url="https://github.com/xavierbastidas",age=22),
             User(id=2,name="jonathan",surname="bastidas",url="https://github.com/xavierbastidas",age=22),
             User(id=3,name="jona",surname="bastidas",url="https://github.com/xavierbastidas",age=22)
             ]



@router.get("/api/v2/usersjson")
async def usersjson():
    return  [{"name":"xavier",
              "id":1,
             "surname":"bastidas",
             "url":"https://github.com/xavierbastidas",
             "age":22
             },
             {"name":"jonathan",
              "id":2,
             "surname":"bastidas",
             "url":"https://github.com/xavierbastidas",
             "age":22
             },
             
             {"name":"jona",
              "id":3,
             "surname":"bastidas",
             "url":"https://github.com/xavierbastidas",
             "age":22 }
             ]

@router.get("/api/v2/users")
async def users():
    return users_list

#Usar parametros de ruta para traer un recurso fijo
@router.get("/api/v2/user/{ide}")
async def user(ide:int):
    return search_user(ide)
 
 #Usar query cuando quiero filtar los atributos de un recurso  , 
 #Para realizar la paginacion de datos
 #http://127.0.0.1:8000/api/v2/user/?id=1&name=jonathan

@router.get("/api/v2/user/")
async def user(id:int):
    return search_user(id)



@router.post("/api/v2/user/",response_model=User,status_code=201)
async def user(user:User):
    if type(search_user(user.id))==User:
       raise HTTPException(status_code=404,detail="El usario ya existe")
    users_list.append(user)
    return user


@router.put("/api/v2/user/")
async def user(user:User):
    for index , saved_user in  enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index]=user
            return user
        return {"error":"No se ha podido actualizar el usuario"}

@router.delete("/api/v2/user/{id}")
async def user(id:int):
    for user in users_list:
        if user.id==id:
            users_list.remove(user)
            return users_list
        return {"error":"No se ha podido eliminar el usuario"}
        

def search_user(id:int):
     users = filter(lambda user :user.id==id,users_list)
     try:
        return  list(users)[0]
     except Exception as error:
       return {"error":str(error)}


        
        
   



