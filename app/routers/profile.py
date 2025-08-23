# app/routers/profile.py
from fastapi import APIRouter
from app.s3 import get_profile, put_json, clear_caches, STUDENT_ID

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("")
def read_profile():
    return get_profile()

@router.patch("")
def update_profile(partial: dict):
    profile = get_profile().copy()
    profile.update(partial)
    put_json(f"students/{STUDENT_ID}/profile.json", profile)
    clear_caches()
    return profile