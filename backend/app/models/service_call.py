from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SQLEnum

from .base import Base
from .enums import Service_Call_Priority, Service_Call_Status


if TYPE_CHECKING:
    from .branch import Branch
    from .technician import Technician
    from .atm import ATM
    from .diagnostic_report import DiagnosticReport

class ServiceCall(Base):
    __tablename__="service_calls"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    priority: Mapped[Service_Call_Priority] = mapped_column(
        SQLEnum(
        name="Service call priority",
        values_callable=lambda enum_cls: [member.value for member in enum_cls],
        ), default=Service_Call_Priority.LOW
    )
    status: Mapped[Service_Call_Status] = mapped_column(
        SQLEnum(
            name="Service call status",
            values_callable=lambda enum_cls: [member.value for member in enum_cls]
        ), default=Service_Call_Status.IN_PROGRESS
    )
    atm_id: Mapped[int] = mapped_column(Integer, ForeignKey("atms.id"))
    technician_id: Mapped[int] = mapped_column(Integer, ForeignKey("technicians.id"))

    branch: Mapped["Branch"] = relationship(back_populates="service_calls")
    technician: Mapped["Technician"] = relationship(back_populates="service_calls")
    atm: Mapped["ATM"] = relationship(back_populates="service_calls")
    diagnostic_report: Mapped["DiagnosticReport"] = relationship(back_populates="service_calls")

    def __repr__(self):
            return(f"{ServiceCall.id}, {ServiceCall.title}, {ServiceCall.priority}, {ServiceCall.status}, {ServiceCall.atm_id}, {ServiceCall.technician_id}")