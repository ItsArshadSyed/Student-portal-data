# app/s3.py
import os, json
from functools import lru_cache
from dotenv import load_dotenv
import boto3
from typing import Union

load_dotenv()

S3_BUCKET  = os.getenv("S3_BUCKET")
ENV        = os.getenv("ENVIRONMENT", "production")
STUDENT_ID = os.getenv("STUDENT_ID", "s-001")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

s3 = boto3.client("s3", region_name=AWS_REGION)

def _key(rel: str) -> str:
    return f"{rel}"

def get_json(key_rel: str):
    obj = s3.get_object(Bucket=S3_BUCKET, Key=_key(key_rel))
    return json.loads(obj["Body"].read())

def put_json(key_rel: str, data: Union[dict, list]):
    s3.put_object(
        Bucket=S3_BUCKET,
        Key=_key(key_rel),
        Body=json.dumps(data).encode("utf-8"),
        ContentType="application/json"
    )

@lru_cache(maxsize=64)
def get_courses():
    return get_json(f"students/{STUDENT_ID}/courses.json")

@lru_cache(maxsize=64)
def get_assignments():
    return get_json(f"students/{STUDENT_ID}/assignments.json")

@lru_cache(maxsize=64)
def get_profile():
    return get_json(f"students/{STUDENT_ID}/profile.json")

def clear_caches():
    get_courses.cache_clear()
    get_assignments.cache_clear()
    get_profile.cache_clear()