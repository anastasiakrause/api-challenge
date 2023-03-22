from fastapi import FastAPI, APIRouter, HTTPException, Depends
from typing import Union, List
from pathlib import Path
from sqlalchemy.orm import Session

from datetime import datetime
from fastapi_pagination import Page, add_pagination, paginate
from app.schemas.vehicle import VehicleData, VehicleDataSearchResults, VehicleDataCreate
from app.crud.crud_vehicle import crud_vehicle
from app import deps
import uuid
from app.core.config import settings
from app.api.api_v1.api import api_router

ROOT = Path(__file__).resolve().parent.parent
BASE_PATH = Path(__file__).resolve().parent

root_router = APIRouter()
app = FastAPI(title="Voltera Challenge: Electric Vehicle API")


@root_router.get("/", status_code=200, response_model=Page[VehicleData])
def root(db: Session = Depends(deps.get_db)):
    """
    Root GET: fetches all data.
    """

    result = crud_vehicle.get_multi(db=db)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"DB table not found."
        )

    return paginate(result)

add_pagination(app)
app.include_router(root_router, prefix=settings.API_V1_STR)
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
