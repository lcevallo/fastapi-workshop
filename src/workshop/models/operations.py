from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum

from pydantic import BaseModel


class Operationkind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    data: date
    kind: Operationkind
    amount: Decimal
    description: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase):
    pass
