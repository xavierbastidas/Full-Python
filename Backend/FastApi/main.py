from fastapi import FastAPI
from routers import products,users
from fastapi.staticfiles import StaticFiles
app=FastAPI()
#Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/api/v2/static",StaticFiles(directory="static"),name="static")

@app.get("/api/v2")
async def root():
    return  "!Hola FastAPI!"

@app.get("/api/v2/url")
async def root():
    return  {"url":"https://github.com/xavierbastidas"}

