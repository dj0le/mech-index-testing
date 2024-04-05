from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, or_, select
from contextlib import asynccontextmanager

from sql_app.database import create_db_and_tables, engine
from sql_app.models import mechIndex

app = FastAPI()
app.mount("/static", StaticFiles(directory="mechviewer/static"), name="static")
templates = Jinja2Templates(directory="mechviewer/templates")

# def get_role():
#     with Session(engine) as session:
#         statement = select(mechIndex.types).distinct()
#         distinct_role = session.exec(statement).all()
#         single_role = set()
#         for role in distinct_role:
#             single_role.update(role.split())
#             return single_role

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()
#     yield

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "mechs": [], "types": types}
    )

@app.get("/type/")
def read_mechs_by_type(request: Request, type: str | None = None):
    return