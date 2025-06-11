from fastapi import APIRouter, HTTPException
from app.excel_utils import list_tables, get_table_details, row_sum

router = APIRouter()

@router.get("/list_tables")
def list_tables_endpoint():
    try:
        return list_tables()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_table_details")
def get_table_details_endpoint(sheet_name: str):
    try:
        return get_table_details(sheet_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/row_sum")
def row_sum_endpoint(sheet_name: str, row_index: int):
    try:
        return row_sum(sheet_name, row_index)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
