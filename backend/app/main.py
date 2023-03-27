from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from datetime import datetime
from fastapi_pagination import Page, add_pagination, paginate
from app.schemas.vehicle import VehicleData
from app.crud.crud_vehicle import crud_vehicle
from app.api import deps
from app.core.config import settings
from app.api.api_v1.api import api_router

root_router = APIRouter()
app = FastAPI(title="Voltera Challenge: Electric Vehicle API")

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

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
