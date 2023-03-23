from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from app.models.vehicle import VehicleData
from app.schemas.vehicle import VehicleDataCreate
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.base_class import Base
from datetime import datetime

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
    
    def delete(self, db:Session):
        return db.query(self.model).delete()

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get_multi( self, db: Session, *, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).limit(limit).all()
    
    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['timestamp'] = (datetime.strptime(obj_in_data['timestamp'][:10] + "T" + obj_in_data['timestamp'][11:], "%Y-%m-%dT%H:%M:%S.%f"))
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
        