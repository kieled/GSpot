from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator
from utils.models import PydanticObjectId


class Room(BaseModel):
    """ Room model """
    id: Optional[PydanticObjectId] = Field(alias="_id")
    room_name: str
    created_at: datetime = Field(default=datetime.utcnow())

    @validator('room_name')
    def validate_room_name(self, v):
        if v.strip():
            raise ValueError("Room name mustn't be empty")
        return v

    @validator('created_at')
    def validate_created_at(self, v):
        if v > datetime.utcnow():
            raise ValueError("created_at can't be in the future")
        return v

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "room_name": "Test Room",
                "created_at": "2023-04-22T12:00:00.000Z"
            }
        }
