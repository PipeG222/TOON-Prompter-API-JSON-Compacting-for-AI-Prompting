from pydantic import BaseModel
from typing import Any

class ConvertedResponse(BaseModel):
    mode: str
    original: Any
    result: Any
