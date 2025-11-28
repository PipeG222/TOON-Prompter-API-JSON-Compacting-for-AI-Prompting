from fastapi import APIRouter, Body, Query
from app.converters.toon import convert_json
from app.schemas.response import ConvertedResponse

router = APIRouter()

@router.post("/json", response_model=ConvertedResponse)
def convert(
    payload: dict = Body(...),
    mode: int = Query(3, description="1=compress, 2=optimize, 3=toon")
):
    return convert_json(payload, mode)
