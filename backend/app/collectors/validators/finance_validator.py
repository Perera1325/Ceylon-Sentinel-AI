from typing import Optional

from pydantic import Field

from .base_validator import BaseValidator


class FinanceItemValidator(BaseValidator):
    usd_lkr: float
    eur_lkr: Optional[float] = None
    gbp_lkr: Optional[float] = None
    jpy_lkr: Optional[float] = None
    inr_lkr: Optional[float] = None
    gold_price: Optional[float] = None
    silver_price: Optional[float] = None
    diesel_price: Optional[float] = None
    petrol_price: Optional[float] = None
    exchange_timestamp: str
