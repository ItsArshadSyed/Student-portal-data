# app/routers/courses.py
from fastapi import APIRouter, Query
from app.s3 import get_courses

router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("")
def list_courses(limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)):
    items = get_courses()
    return {"items": items[offset:offset+limit], "total": len(items)}