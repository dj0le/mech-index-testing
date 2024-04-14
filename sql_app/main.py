from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import Field
from contextlib import asynccontextmanager

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="sql_app/static"), name="static")
templates = Jinja2Templates(directory="sql_app/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def get_mech_cards(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mech_short = crud.get_mech_cards(db, skip=skip, limit=limit)
    return templates.TemplateResponse(
        "index.html", {"request": request, 'mech_cards': mech_short}
    )
@app.get("/cardtest/", response_model=list[schemas.Mech])
def get_mech_cards(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = crud.get_mech_cards(db, skip=skip, limit=limit)
    return cards

@app.get("/mechs/", response_model=list[schemas.Mech])
def get_mechs(skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    mechs = crud.get_mechs(db, skip=skip, limit=limit)
    return mechs

@app.get("/mechs/{mech_id}", response_class=HTMLResponse, include_in_schema=False)
def get_mech(request: Request, mech_id: int, db: Session = Depends(get_db)):
    mech_details = crud.get_mech(db, mech_id=mech_id)
    if mech_details is None:
        raise HTTPException(status_code=404, detail="Unknown Mech")
    return templates.TemplateResponse(
        "overview.html", {"request": request, 'mech': mech_details}
    )

@app.get("/test/{mech_id}", response_model=schemas.Mech)
def get_mech(request: Request, mech_id: int, db: Session = Depends(get_db)):
    db_mech = crud.get_mech(db, mech_id=mech_id)
    if db_mech is None:
        raise HTTPException(status_code=404, detail="Unknown Mech")
    return db_mech

@app.get("/images/", response_class=HTMLResponse, include_in_schema=False)
def get_images(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    images = crud.get_images(db, skip=skip, limit=limit)
    return templates.TemplateResponse(
        "images.html", {"request": request, 'mech_images': images}
    )
