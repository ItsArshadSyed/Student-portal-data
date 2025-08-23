# app/models.py
from pydantic import BaseModel
from typing import Optional, Literal

class Course(BaseModel):
    courseId: str
    courseName: str
    creditUnits: int
    letterGrade: Optional[str] = None
    gradePoints: Optional[float] = None

class Assignment(BaseModel):
    assignmentId: str
    courseId: str
    title: str
    status: Literal["Completed","Ongoing"]
    dueDate: str

class Profile(BaseModel):
    studentId: str
    name: str
    email: str
    phone: Optional[str] = None
    semester: Optional[str] = None