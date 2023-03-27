from fastapi import APIRouter , Depends ,HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import datetime , timedelta
from dotenv import load_dotenv 
from os import environ
load_dotenv()

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION=1



# pip install python-jose[cryptography]
# pip install passlib[bcrypt] 
router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

#Hashear  password

crypt = CryptContext(schemes=["bcrypt"])



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
         "password":"$2a$12$jh.Tmf8rWICXrlkaHgUFiuKhUjWqqWEJGq7HdkGQjpBt3zKPNTLPi"  #12345  bcrypt generator
    },
    "jonathan2":{
         "username":"jonathan2",
         "full_name":"Jonathan Bastidas 2",
         "email":"bastidasjonathan140148@gmail.com",
         "disabled":True,
         "password": "$2a$12$6tNjhLN/fIBtu1u3vYSl/OWwMz9hxCjWC6EhGjwxRIv23GuRiEsTm"        #654321
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username]) 
    
async def auth_user(token:str=Depends(oauth2)):
  exception = HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales de autenticacion inavalidas",
          headers={"www.Autenticate":"Bearer"})
  try:
      username = jwt.decode(token,environ.get('SECRET'),algorithms=[ALGORITHM]).get("sub")
      if username is None:
          raise exception
      
          
  except JWTError:
      raise exception
  
  return search_user(username)

   
      
      
      



async def current_user(user:User= Depends(auth_user)):
  if user.disabled:
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST,detail="Usuario inactivo") 
  return user
      


@router.post("/api/v2/jwt/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El usuario no es correcto")
    user =search_user_db(form.username)
    if not crypt.verify(form.password,user.password):
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La contraseña no es correcta")
    
   

    expire  = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

    access_token = {"sub":user.username, "exp":expire}

    return {"access_token":jwt.encode(access_token,environ.get('SECRET'),algorithm=ALGORITHM),"token_type":"bearer"}




@router.get("/api/v2/users/jwt/me")
async def me (user:User =Depends(current_user)):
    return user




