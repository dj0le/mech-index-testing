from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

class Mech(Base):
    __tablename__ = "mwomechs"

    id = Column(Integer, primary_key=True)
    shortName = Column(String)
    chassis = Column(String)
    model = Column(String)
    year = Column(Integer)
    weight = Column(Integer)
    weightClass = Column(String)
    cost = Column(Integer)
    bv = Column(Integer)
    isClan = Column(Boolean, default=False)
    armorType = Column(String)
    totalExternalArmor = Column(Integer)
    totalInternalArmor = Column(Integer)
    structureType = Column(String)
    engine = Column(String)
    heatCapacity = Column(Integer)
    heatSinks = Column(Integer)