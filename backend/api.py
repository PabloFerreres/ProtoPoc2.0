from fastapi import APIRouter
from backend.db import get_all_rows, update_row

router = APIRouter()

@router.get("/projects")
def projects():
    return ["TestBauteile"]

@router.get("/project/{projekt_id}")
def project_detail(projekt_id: str):
    return get_all_rows()

@router.post("/update_row")
async def update_row_api(data: dict):
    return update_row(data)
