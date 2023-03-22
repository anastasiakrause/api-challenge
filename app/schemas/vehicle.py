from pydantic import BaseModel
from datetime import datetime
from typing import List, Union, Sequence, Optional


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

# Properties to receive via API on creation
class VehicleDataCreate(VehicleBase):
    ...


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