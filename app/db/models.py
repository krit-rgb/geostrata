from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class ReviewQueueModel(Base):
    __tablename__ = "review_queue"

    id: Mapped[str] = mapped_column(
        String(100),
        primary_key=True,
    )

    discrepancy_report_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )