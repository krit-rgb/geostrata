from typing import Literal

from pydantic import BaseModel


class DiscrepancyReport(BaseModel):
    report_id: str
    polyhedron_id: str
    status: Literal[
        "match",
        "mismatch",
        "no_existing_record"
    ]
    difference: str | None = None
    human_review_required: bool