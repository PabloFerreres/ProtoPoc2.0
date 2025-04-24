from fastapi import APIRouter, Request
from backend.db import get_all_projects, get_project_data, update_project_row, get_all_master_data, update_master_row_data

router = APIRouter()

@router.get("/projects")
def projects():
    return get_all_projects()

@router.get("/project/{projekt_id}")
def project_detail(projekt_id: str):
    return get_project_data(projekt_id)

@router.post("/update_row")
async def update_row(data: dict):
    # Erwartet keys: call_id, projekt_id, Bauteil, Revision, Beschreibung
    return update_project_row(data)

@router.get("/master")
def master_data():
    return get_all_master_data()

@router.post("/update_master_row")
async def update_master_row(data: dict):
    return update_master_row_data(data)
