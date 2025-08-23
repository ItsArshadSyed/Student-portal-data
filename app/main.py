# app/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Student Portal API")

origins = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if origins == ["*"] else origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import health, auth, profile, dashboard, courses, cgpa, assignments  # noqa

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(dashboard.router)
app.include_router(courses.router)
app.include_router(cgpa.router)
app.include_router(assignments.router)

# Optional Lambda adapter
handler = None
if os.getenv("LAMBDA_WRAPPER", "0") == "1":
    from mangum import Mangum
    handler = Mangum(app)