import logging
from sqlalchemy.orm import Session

from app.crud.crud_vehicle import crud_vehicle
from app.schemas.vehicle import VehicleDataCreate
from app.db import base   # noqa: F401
from app.db.base_class import Base
from datetime import datetime
from db.session import engine
from vehicle_data import load_vehicle_data
logger = logging.getLogger(__name__)

def init_db(db: Session) -> None:
    # Create database schemas
    Base.metadata.create_all(bind=engine)

    # Load vehicle data from local data/ folder into variable
    VEHICLES = load_vehicle_data()

    # Add each local record to database
    for vehicle in VEHICLES:
        vehicle_in = VehicleDataCreate(
            vehicle_id=vehicle["vehicle_id"],
            timestamp=datetime.fromisoformat(vehicle["timestamp"]),
            speed=vehicle["speed"],
            odometer=vehicle["odometer"],
            soc=vehicle["soc"],
            elevation=vehicle["elevation"],
            shift_state=vehicle["shift_state"],
        )
        crud_vehicle.create(db, obj_in=vehicle_in)