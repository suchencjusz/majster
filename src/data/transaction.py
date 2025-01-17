from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator
from .enums.currency import Currency
from .enums.operation_type import OperationType

class Transaction(BaseModel):
    date_operation: datetime
    date_value: datetime
    amount: float = Field(...)
    currency: Currency
    description: str
    operation_type: OperationType = OperationType.UNKNOWN
    category: Optional[str] = None
    raw_operation_type: Optional[str] = None
    extra_data: Dict[str, Any] = Field(default_factory=dict)

    @field_validator('currency')
    def validate_currency(cls, v):
        if isinstance(v, str):
            return Currency(v)
        return v

    @field_validator('amount')
    def validate_amount(cls, v):
        return float(v)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            Currency: lambda v: v.value,
            OperationType: lambda v: v.value
        }