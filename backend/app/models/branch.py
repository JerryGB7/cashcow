from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .atm import ATM


class Branch(Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[int] = mapped_column(String(50))
    location_region: Mapped[str] = mapped_column(String(70))
    capacity: Mapped[int] = mapped_column(Integer)
    supervisor_id: Mapped[int] = mapped_column(Integer) 

    atms: Mapped[ATM] = relationship(back_populates="branches")


    def __repr__(self):
        return(f"{Branch.id}, {Branch.name}, {Branch.location_region}, {Branch.capacity}, {Branch.supervisor_id}")