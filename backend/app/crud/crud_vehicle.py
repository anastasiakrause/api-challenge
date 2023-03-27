from app.crud.base import CRUDBase
from app.models.vehicle import VehicleData
from app.schemas.vehicle import VehicleDataCreate
from sqlalchemy.orm import Session

class CRUDVehicle(CRUDBase[VehicleData, VehicleDataCreate]):
    ...

crud_vehicle = CRUDVehicle(VehicleData)
