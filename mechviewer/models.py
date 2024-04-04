from sqlmodel import Field, SQLModel

class mechList(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tons: int
    bv: str
    pv: int
    types: str
    intro: int

class mechIndex(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    shortName: str
    chassis: str
    model: str
    year: str
    weight: int
    weightClass: str
    cost: int
    bv: int
    isClan: str
    armorType: str
    totalExternalArmor: str
    totalInternalArmor: str
    structureType: str
    engine: str
    heatCapacity: int
    heatSinks: int
    
    
    