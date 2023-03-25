from typing import Any, Union, List
from datetime import datetime
from operator import attrgetter
import re

def filter_vehicle_data(
        payload : List,
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
        payload : List,
        sort_parameter : str,
):
    """
    Helper sort function: sorts payload based on vehicle parameter.
    """
    
    payload.sort(key = attrgetter(sort_parameter), reverse=True)
    return payload

def validate_vehicle_id(vehicle_id):
    """
    Ensure vehicle_id is a valid ID
    """
    
    pattern = r"[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+"
    return bool(re.match(pattern, vehicle_id))

def validate_timestamp_iso(timestamp):
    """
    Ensure timestamp valid ISO format
    """

    pattern = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    match_iso8601 = re.compile(pattern).match
    try:            
        if match_iso8601( timestamp ) is not None:
            return True
    except:
        pass
    return False