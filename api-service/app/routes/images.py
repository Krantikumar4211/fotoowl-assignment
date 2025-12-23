from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.image import Image

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/import/google-drive")
def import_google_drive(payload: dict):
    """
    Accepts Google Drive folder URL
    Push job to queue (logic added Day 3)
    """
    return {
        "status": "accepted",
        "message": "Import job queued successfully"
    }

@router.get("/images")
def get_images(db: Session = Depends(get_db)):
    images = db.query(Image).all()
    return images
