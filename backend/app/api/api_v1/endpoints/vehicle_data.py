from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Union
from datetime import datetime

from app.crud.crud_vehicle import crud_vehicle
from app.api import deps
from app.schemas.vehicle import VehicleData, VehicleDataCreate
from fastapi_pagination import Page, paginate
from app.api.helpers import filter_vehicle_data, sort_vehicle_data

router = APIRouter()

@router.get("/", status_code=200, response_model=Page[VehicleData])
def get_all_data(db: Session = Depends(deps.get_db)):
    """
    Root GET: fetches all data.
    """

    result = crud_vehicle.get_multi(db=db)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"DB table not found."
        )

    return paginate(result)


@router.get("/{vehicle_id}", status_code=200, response_model=Page[VehicleData])
def get_vehicle_data(
               vehicle_id: str,
               start : Union[datetime, None] = None,
               end : Union[datetime, None] = None,
               limit : Union[int, None] = None,
               sort_by : str = None,
               db: Session = Depends(deps.get_db),
            ):
    """
    Search for vehicle data information by vehicle ID.
    Also able to specify data further by start datetime, end datetime, return limit, and sort attribute.
    """

    vehicles = crud_vehicle.get_multi(db=db)

    if not vehicles:
        raise HTTPException(
            status_code=404, detail=f"Vehicle with ID {vehicle_id} not found."
        )
    
    results = list(filter(lambda vehicle: vehicle_id == vehicle.vehicle_id, vehicles))
    
    if start or end or limit: results = filter_vehicle_data(results, start, end, limit)
    
    if sort_by: results = sort_vehicle_data(results, sort_by)
    
    return paginate(results)

@router.post("/", status_code=201, response_model=VehicleData)
def create_vehicle(
    *, db: Session = Depends(deps.get_db), vehicle_data_in: VehicleDataCreate
):
    """
    Create a new Vehicle Data entry.
    """

    vehicle_entry = VehicleDataCreate(
        vehicle_id=vehicle_data_in.vehicle_id,
        timestamp=vehicle_data_in.timestamp,
        speed=vehicle_data_in.speed,
        odometer=vehicle_data_in.odometer,
        soc=vehicle_data_in.soc,
        elevation=vehicle_data_in.elevation,
        shift_state=vehicle_data_in.shift_state,
    )
    
    crud_vehicle.create(db, obj_in=vehicle_entry)
    return vehicle_entry