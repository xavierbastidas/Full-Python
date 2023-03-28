from fastapi import APIRouter,HTTPException,status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema , users_schema
from bson import ObjectId

router = APIRouter(prefix="/api/v2/userdb",
                   tags= ["userdb"],
                   responses={status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}})


def search_user(field:str,key):
    try:
      user= db_client.users.find_one({field:key})
      return User(**user_schema(user))
    except:
      return {"error":"No se ha encontrado el usuario"}

@router.get("/",response_model=list[User])
async def users():
   return users_schema(db_client.users.find())



@router.get("/{ide}") #Path
async def user(ide:str):
    return search_user("_id",ObjectId(ide))



@router.get("/")  # Query?id=642108280d978defbcfae688
async def user(id:str):
    return search_user("_id",ObjectId(id))



@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def user(id:str):
        found=db_client.users.find_one_and_delete({"_id":ObjectId(id)})
        if not found:
          return {"error":"No se ha eliminado el usuario"}


@router.post("/",response_model=User,status_code=status.HTTP_201_CREATED)
async def user(user:User):

    if type(search_user("email",user.email))==User:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El usario ya existe")
    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.users.find_one({"_id":id}))
    return User(**new_user)


@router.put("/")
async def user(user:User):
        try:
            user_dict = dict(user)
            del user_dict["id"]
            db_client.users.find_one_and_replace({"_id":ObjectId(user.id)},user_dict)
        except:
            return {"error":"No se ha podido actualizar el usuario"}
        
        return  search_user("_id",ObjectId(user.id))

        


        



