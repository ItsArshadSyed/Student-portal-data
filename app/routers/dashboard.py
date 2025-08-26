from fastapi import APIRouter
from app.s3 import get_profile

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("")
def overview():
    """3-panel dashboard data straight from profile.json."""
    p = get_profile() or {}

    return {
        "personal": {
            "name": p.get("personal", {}).get("name", ""),
            "id": p.get("personal", {}).get("id", ""),
            "phone": p.get("personal", {}).get("phone", ""),
            "email": p.get("personal", {}).get("email", ""),
        },
        "degreeProgress": {
            "bachelors": p.get("degreeProgress", {}).get("bachelors", ""),
            "discipline": p.get("degreeProgress", {}).get("discipline", ""),
            "joinDate": p.get("degreeProgress", {}).get("joinDate", ""),
        },
        "graduation": {
            "email": p.get("graduation", {}).get("email", ""),
            "phone": p.get("graduation", {}).get("phone", ""),
            "alternateEmail": p.get("graduation", {}).get("alternateEmail", ""),
            "address": p.get("graduation", {}).get("address", ""),
        },
        "adminNotifications": {
            "feePayment": p.get("adminNotifications", {}).get("feePayment", ""),
            "lastDate": p.get("adminNotifications", {}).get("lastDate", ""),
            "uploadCertificate": p.get("adminNotifications", {}).get("uploadCertificate", False),
            "pendingStatus": p.get("adminNotifications", {}).get("pendingStatus", ""),
        },
        "transfer": p.get("transfer", []),
    }