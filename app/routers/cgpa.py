# app/routers/cgpa.py
from fastapi import APIRouter
from app.s3 import get_courses

router = APIRouter(prefix="/cgpa", tags=["cgpa"])

@router.get("")
def get_cgpa():
    courses = get_courses()
    sum_w = sum((c.get("gradePoints") or 0) * c.get("creditUnits", 0) for c in courses)
    sum_c = sum(c.get("creditUnits", 0) for c in courses if c.get("gradePoints") is not None)
    cgpa = round(sum_w / sum_c, 2) if sum_c else 0.0
    return {"cgpa": cgpa, "sumWeighted": sum_w, "sumCredits": sum_c,
            "formula": "sum(gradePoints*creditUnits)/sum(creditUnits)"}