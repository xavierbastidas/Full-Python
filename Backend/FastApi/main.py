from fastapi import FastAPI
app=FastAPI()

@app.get("/api/v2")
async def root():
    return  "!Hola FastAPI!"

@app.get("/api/v2/url")
async def root():
    return  {"url":"https://github.com/xavierbastidas"}

