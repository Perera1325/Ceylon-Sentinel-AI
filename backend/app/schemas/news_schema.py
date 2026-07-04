import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class NewsBase(BaseModel):
    title: str = Field(..., description="The headline of the news article", example="Tsunami Warning Issued")
    summary: Optional[str] = Field(None, description="A brief summary of the article", example="Coastal areas are advised to evacuate.")
    content: Optional[str] = Field(None, description="Full content of the news article")
    category: Optional[str] = Field(None, description="News category (e.g., Disaster, Politics)", example="Disaster")
    author: Optional[str] = Field(None, description="Author or publisher", example="National News Agency")
    source: str = Field(..., description="Source URL or name", example="news.lk")
    image_url: Optional[str] = Field(None, description="URL of the main image")
    published_date: Optional[str] = Field(None, description="Date the article was published")
    url: str = Field(..., description="Direct link to the original article")
    language: str = Field("en", description="Language code")
    district: Optional[str] = Field(None, description="Associated district in Sri Lanka", example="Colombo")
    country: str = Field("Sri Lanka", description="Country context")
    hash: str = Field(..., description="Unique hash of the content to prevent duplicates")


class NewsResponse(NewsBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
