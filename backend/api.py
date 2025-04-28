from fastapi import APIRouter
from backend.db import get_all_rows, update_row, save_layout

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

@router.post("/save_layout")
async def save_layout_api(data: dict):
    projekt_id = data.get("projekt_id", "TestBauteile")
    view_type = data.get("view_type", "project")
    column_settings = data.get("column_settings", {})

    return save_layout(projekt_id, view_type, column_settings)

@router.get("/layout/{projekt_id}")
def get_layout(projekt_id: str):
    from backend.db import load_layout
    return load_layout(projekt_id, "project")
