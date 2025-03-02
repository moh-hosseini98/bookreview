from fastapi import FastAPI


app = FastAPI()


@app.get("/info")
async def root():
    return {"message":"hello-world","version":"1.0.0"}