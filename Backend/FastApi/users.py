from fastapi import FastAPI
app=FastAPI()

@app.get("/api/v2/users")
async def root():
    return  "!Hola FastAPI!"
