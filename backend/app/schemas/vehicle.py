from pydantic import BaseModel, validator
from datetime import datetime
from typing import Sequence, Optional
from app.api.helpers import validate_vehicle_id, validate_timestamp_iso


class VehicleBase(BaseModel):
    vehicle_id : str
    timestamp: datetime
    speed: str
    odometer: float
    soc: int
    elevation: int
    shift_state: str

    class config:
        schema_extra = {
            "example": {
                "timestamp": datetime.fromisoformat("2022-07-12T18:00:16.981000"),
                "speed": "22",
                "odometer": 478.2,
                "soc": 2,
                "elevation": 5,
                "shift_state": "D",
            }
        }

# Properties to receive via API on creation with validation
class VehicleDataCreate(VehicleBase):
    @validator('vehicle_id')
    def vehicle_id_matches(cls, v):
        if not validate_vehicle_id(v):
            raise ValueError('Invalid vehicle ID')
        return v
        
    @validator('shift_state')
    def valid_shift_state(cls, v):
        if not len(v) in (1, 4):
            raise ValueError('Shift state must be single char or NULL')
        return v
        
    @validator('odometer')
    def valid_odometer(cls, v):
        if v < 0:
            raise ValueError('Odometer value must be positive')
        return v
    
    @validator('timestamp')
    def valid_timestamp(cls, v):
        if not validate_timestamp_iso(v):
            raise ValueError("Timestamp string not in ISO format")
        return v

# Properties shared by models stored in DB
class VehicleInDBBase(VehicleBase):
    id: Optional[int]

    class Config:
        orm_mode = True

# Properties to return to client
class VehicleData(VehicleInDBBase):
    pass

class VehicleDataSearchResults(BaseModel):
    results: Sequence[VehicleData]