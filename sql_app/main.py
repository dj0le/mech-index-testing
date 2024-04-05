from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# app.mount("/static", StaticFiles(directory="sql_app/static"), name="static")
templates = Jinja2Templates(directory="sql_app/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def list_mechs(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "list_mechs": "imagine a list of mechs by name"}
    )

@app.get("/mechs/", response_model=list[schemas.Mech])
def read_mechs(skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    mechs = crud.get_mechs(db, skip=skip, limit=limit)
    return mechs

@app.get("/mechs/{mech_id}", response_model=schemas.Mech)
def read_mech(mech_id: int, db: Session = Depends(get_db)):
    db_mech = crud.get_mech(db, mech_id=mech_id)
    if db_mech is None:
        raise HTTPException(status_code=404, detail="Unknown Mech")
    return db_mech
