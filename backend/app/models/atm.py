from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, CheckConstraint, ForeignKey
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .enums import ATMStatus

# todo add the if type_checking to connect the branch, technician and service calls to the atms
if TYPE_CHECKING:
   from .branch import Branch
   from .technician import Technician
   from .service_call import ServiceCall

class ATM(Base):
    __tablename__ = "atms"

    __table_args__ = CheckConstraint("cash_level BETWEEN 0 AND 100", name="cash_level_range" )

    id: Mapped[int] = mapped_column(primary_key=True)
    serial_number: Mapped[int] = mapped_column(Integer)
    model: Mapped[str] = mapped_column(String,(50))

    status: Mapped[ATMStatus] = mapped_column(
        SQLEnum(ATMStatus, name="atm_status",
        values_callable=lambda enum_cls: [member.value for member in enum_cls],
        ), default=ATMStatus.OPERATIONAL
    )
    cash_level: Mapped[int] = mapped_column(Integer)
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))
    technician_id: Mapped[int] = mapped_column(Integer, ForeignKey("technicians.id"))

    # TODO create the realtions between the branch, technician, and service call models
    branch: Mapped["Branch"] = relationship(back_populates="atms")
    technician: Mapped["Technician"] = relationship(back_populates="atms")
    service_call: Mapped["ServiceCall"] = relationship(back_populates="atm")

    # representing as a string for logging and debugging
    def __repr__(self):
        return(f"{ATM.id}, {ATM.serial_number}, {ATM.model}, {ATM.status}, {ATM.cash_level}, {ATM.branch_id}, {ATM.technician_id}")

