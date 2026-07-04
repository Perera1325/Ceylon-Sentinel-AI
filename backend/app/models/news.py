from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import BaseModel


class News(BaseModel):
    __tablename__ = "news"

    title: Mapped[str] = mapped_column(String(500), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    category: Mapped[str] = mapped_column(String(100), nullable=True)
    author: Mapped[str] = mapped_column(String(200), nullable=True)
    source: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
    published_date: Mapped[str] = mapped_column(String(50), nullable=True)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    language: Mapped[str] = mapped_column(String(10), default="en")
    district: Mapped[str] = mapped_column(String(100), nullable=True)
    country: Mapped[str] = mapped_column(String(100), default="Sri Lanka")
    hash: Mapped[str] = mapped_column(
        String(64), unique=True, nullable=False, index=True
    )
