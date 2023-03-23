from fastapi import APIRouter

from app.api.api_v1.endpoints import vehicle_data

api_router = APIRouter()
api_router.include_router(vehicle_data.router, prefix="/vehicle_data", tags=["vehicles"])