from typing import Optional

from pydantic import Field

from .base_validator import BaseValidator


class NewsItemValidator(BaseValidator):
    title: str = Field(..., min_length=1)
    summary: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    image_url: Optional[str] = None
    published_date: str
    author: Optional[str] = None
    category: Optional[str] = None
    original_url: str = Field(..., min_length=5)
    language: str = Field(default="en")
    district: Optional[str] = None
    country: str = Field(default="Sri Lanka")
