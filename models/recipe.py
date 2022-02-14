from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Boolean
from database.db import Base


class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    image = Column(String)
    cartegory = Column(String)


class Step(Base):
    pass
