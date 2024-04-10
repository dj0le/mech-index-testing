from pydantic import BaseModel

class MechBase(BaseModel):
    id: int

class Mech(MechBase):
    shortName: str
    chassis: str
    model: str
    year: int
    weight: int
    weightClass: str
    cost: int
    bv: int
    isClan: bool
    armorType: str
    totalExternalArmor: int
    totalInternalArmor: int
    structureType: str
    engine: str
    heatCapacity: int
    heatSinks: int
    thumbnail: str
    image: str

    class Config:
        orm_mode = True


class ImageBase(BaseModel):
    id: int

class Image(ImageBase):
    imageFileName: str
    thumbnail: str

    class Config:
        orm_mode = True