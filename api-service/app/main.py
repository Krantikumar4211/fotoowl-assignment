from fastapi import FastAPI
from app.database import Base, engine
from app.routes import images

#Base.metadata.create_all(bind=engine)

app = FastAPI(title="Foto Owl Image Import API")

app.include_router(images.router)

@app.get("/")
def root():
    return {"message": "Foto Owl API is running"}
