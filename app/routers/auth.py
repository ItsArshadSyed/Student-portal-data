# app/routers/auth.py
from fastapi import APIRouter
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/change-password")
def change_password(payload: dict):
    return {"ok": True}