from pydantic import BaseModel
from enum import Enum

class NotificationType(str, Enum):
    email = "email"
    sms = "sms"
    in_app = "in-app"

class NotificationCreate(BaseModel):
    user_id: int
    type: NotificationType
    content: str

class Notification(NotificationCreate):
    id: str
    status: str

    class Config:
        orm_mode = True
