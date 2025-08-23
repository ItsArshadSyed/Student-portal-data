# app/routers/assignments.py
from fastapi import APIRouter, Query
from typing import Optional, Literal
from app.s3 import get_assignments

router = APIRouter(prefix="/assignments", tags=["assignments"])

@router.get("")
def list_assignments(
    status: Optional[Literal["Completed","Ongoing"]] = None,
    courseId: Optional[str] = None,
    assignmentId: Optional[str] = None,
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    items = get_assignments()
    if status:
        items = [a for a in items if a.get("status") == status]
    if courseId:
        items = [a for a in items if a.get("courseId") == courseId]
    if assignmentId:
        items = [a for a in items if a.get("assignmentId") == assignmentId]
    return {"items": items[offset:offset+limit], "total": len(items)}