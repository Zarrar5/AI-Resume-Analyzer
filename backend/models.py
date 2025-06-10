from typing import List
from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    fit_score: float
    matched_keywords: List[str]
    missing_keywords: List[str]
    suggestions: List[str]
