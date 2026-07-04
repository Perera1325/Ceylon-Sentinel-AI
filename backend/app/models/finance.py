from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import BaseModel


class Finance(BaseModel):
    __tablename__ = "finance"

    currency: Mapped[str] = mapped_column(String(10), nullable=True)
    exchange_rate: Mapped[float] = mapped_column(Float, nullable=True)
    gold_price: Mapped[float] = mapped_column(Float, nullable=True)
    silver_price: Mapped[float] = mapped_column(Float, nullable=True)
    fuel_price: Mapped[float] = mapped_column(Float, nullable=True)
    timestamp: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
