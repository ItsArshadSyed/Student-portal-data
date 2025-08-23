# app/routers/dashboard.py
from fastapi import APIRouter
from datetime import date
from app.s3 import get_courses, get_assignments

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("")
def dashboard():
    courses = get_courses()
    assigns = get_assignments()
    completed = [a for a in assigns if a.get("status") == "Completed"]
    ongoing = [a for a in assigns if a.get("status") == "Ongoing"]

    sum_w = sum((c.get("gradePoints") or 0) * c.get("creditUnits", 0) for c in courses)
    sum_c = sum(c.get("creditUnits", 0) for c in courses if c.get("gradePoints") is not None)
    cgpa = round(sum_w / sum_c, 2) if sum_c else 0.0

    today = date.today().isoformat()
    upcoming = sorted([a for a in ongoing if a.get("dueDate") and a["dueDate"] >= today],
                      key=lambda x: x["dueDate"])
    next_due = upcoming[0] if upcoming else None

    return {
        "totalCourses": len(courses),
        "completedAssignments": len(completed),
        "ongoingAssignments": len(ongoing),
        "currentCgpa": cgpa,
        "upcomingDueCount": len(upcoming),
        "nextDue": next_due
    }