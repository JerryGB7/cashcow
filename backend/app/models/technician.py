from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .branch import Branch
    from .atm import ATM
    from .service_call import ServiceCall

class Technician(Base):
    __tablename__="technicians"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    branch_id: Mapped[int] = mapped_column(Integer, ForeignKey("branches.id"))

    branch: Mapped[Branch] = relationship(back_populates="technicians")
    atms: Mapped[list[ATM]] = relationship(back_populates="technician")
    ServiceCall: Mapped[list[ServiceCall]] = relationship(back_populates="technician")

    def __repr__(self):
            return(f"{Technician.id}, {Technician.name}, {Technician.branch_id}")