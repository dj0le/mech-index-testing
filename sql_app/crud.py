from sqlalchemy.orm import Session

from . import models

def get_mech(db: Session, mech_id: int):
    return db.query(models.Mech).filter(models.Mech.id == mech_id).first()

def get_mech_by_model(db: Session, mech_model: str):
    return db.query(models.Mech).filter(models.Mech.model == mech_model).first()

def get_mechs(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Mech).offset(skip).limit(limit).all()

def get_mech_cards(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Mech.id, models.Mech.chassis, models.Mech.weightClass, models.Mech.year).offset(skip).limit(limit).all()
    
def get_images(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.Image).offset(skip).limit(limit).all()