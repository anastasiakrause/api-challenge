from typing import Any, Union, List
from datetime import datetime
from app.schemas.vehicle import VehicleData
from operator import attrgetter

def filter_vehicle_data(
        payload : List[VehicleData],
        start : Union[datetime, None] = None,
        end : Union[datetime, None] = None,
        limit : Union[int, None] = None,
):
    """
    Helper filter function: filters payload based on optional start, end, and limit params.
    """
    
    if start: payload = [p for p in payload if p.timestamp >= start.replace(tzinfo=None)]
    if end: payload = [p for p in payload if p.timestamp <= end.replace(tzinfo=None)]
    if limit and len(payload) > limit: payload = payload[:limit]

    return payload


def sort_vehicle_data(
        payload : List[VehicleData],
        sort_parameter : str,
):
    """
    Helper sort function: sorts payload based on vehicle parameter.
    """
    
    payload.sort(key = attrgetter(sort_parameter), reverse=True)
    return payload