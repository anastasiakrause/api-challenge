from sqlalchemy import Column, Integer, String, DateTime, Float

from app.db.base_class import Base

class VehicleData(Base):
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    speed = Column(String, nullable=False)
    odometer = Column(Float, nullable=False)
    soc = Column(Integer, nullable=False)
    elevation = Column(Integer, nullable=False)
    shift_state = Column(String, nullable=False)