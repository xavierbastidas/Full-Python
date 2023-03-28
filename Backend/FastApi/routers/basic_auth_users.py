from fastapi import APIRouter , Depends ,HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):
    password:str

users_db={
    "jonathan":{
         "username":"jonathan",
         "full_name":"Jonathan Bastidas",
         "email":"bastidasjonathan140148@gmail.com",
         "disabled":False,
         "password":12345
    },
    "jonathan2":{
         "username":"jonathan2",
         "full_name":"Jonathan Bastidas 2",
         "email":"bastidasjonathan140148@gmail.com",
         "disabled":True,
         "password":654321
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username]) 


async def current_user(token:str = Depends(oauth2)):
  user=  search_user(token)
  if not user:
      raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales de autenticacion invalidas",
          headers={"www.Autenticate":"Bearer"})
  
  if user.disabled:
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario inactivo")
      
  return user

@router.post("/api/v2/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The user is not correct")
    user =search_user_db(form.username)
    if not form.password==user.password:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The password is not correct")
    return {"access_token":user.username,"token_type":"bearer"}

@router.get("/api/v2/users/me")
async def me (user:User =Depends(current_user)):
    return user



