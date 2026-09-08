from typing import Literal

from pydantic import BaseModel


class ReviewDecision(BaseModel):
    decision_id: str | None = None
    report_id: str | None = None

    decision: Literal[
        "approved",
        "corrected",
        "rejected"
    ]

    reviewer_id: str
    notes: str