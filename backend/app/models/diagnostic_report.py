from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import String, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .service_call import ServiceCall

class DiagnosticReport(Base):
    __tablename__="diagnostic_reports"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_url: Mapped[str] = mapped_column(String(500))
    notes: Mapped[str | None] = mapped_column(text, nullable=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    service_call: Mapped["ServiceCall"] = relationship(back_populates="diagnostic_reports")
    
    def __repr__(self) -> str:
        return (f"DiagnosticReport(id={self.id}, service_call_id={self.service_call_id}, "
                f"file_url={self.file_url!r})")