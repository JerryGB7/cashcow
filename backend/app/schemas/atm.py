from pydantic import BaseModel, Field, ConfigDict
from app.models.atm import ATMStatus

class ATMBase(BaseModel):
    serial_number: int
    model: str = Field(min_length=1, max_length=50)
    status: ATMStatus = ATMStatus.OPERATIONAL
    cash_level: int = Field(ge=0, le=100)
    branch_id: int
    technician_id: int | None = None

class ATMCreate(ATMBase):
    """Shape of the request body for POST /atms"""

class ATMRead(ATMBase):
    id: int
    model_config= ConfigDict(from_attributes=True)

