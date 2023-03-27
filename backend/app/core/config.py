from pydantic import AnyHttpUrl, BaseSettings, validator
from typing import List, Optional, Union
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # Prefix string for API versioning
    API_V1_STR: str = "/api/v1"

    # Allow requests from:
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8001",  # type: ignore
    ]

    # Origins that match this regex OR are in the above list are allowed
    # For future deployment
    BACKEND_CORS_ORIGIN_REGEX: Optional[
        str
    ] = "https.*\.(netlify.app|herokuapp.com)"  # noqa: W605

    @validator("BACKEND_CORS_ORIGINS", pre=True)  # 3
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # Database URI
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite://vehicle_data.db"

    class Config:
        case_sensitive = True

settings = Settings()
