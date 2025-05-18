from fastapi import APIRouter, HTTPException
from app.database import notifications_collection
from app.schemas import NotificationCreate, Notification
from app.queue import send_to_queue 
from app.schemas import NotificationCreate
from bson import ObjectId

router = APIRouter()

@router.post("/notifications")
async def send_notification(notification: NotificationCreate):
    await send_to_queue(notification.dict())  
    return {"status": "Notification queued"}
@router.get("/users/{user_id}/notifications")
async def get_user_notifications(user_id: int):
    notifs = notifications_collection.find({"user_id": user_id})
    return [
        {
            "id": str(n["_id"]),
            "user_id": n["user_id"],
            "type": n["type"],
            "content": n["content"],
        }
        async for n in notifs
    ]
