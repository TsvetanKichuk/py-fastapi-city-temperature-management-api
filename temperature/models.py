from pydantic.v1 import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship


class Temperature(BaseModel):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True)
    city_id_ = Column(Integer, ForeignKey("city.id"))
    date_time = Column(DateTime)
    temperature = Column(Float)

    city = relationship("City")
