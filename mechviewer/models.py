from sqlmodel import Field, SQLModel, create_engine

class mechList(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tons: int
    bv: str
    pv: int
    types: str
    intro: int

