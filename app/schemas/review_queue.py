from typing import Literal

from pydantic import BaseModel


class ReviewQueueItem(BaseModel):
    id: str
    discrepancy_report_id: str
    status: Literal[
        "pending",
        "reviewed"
    ]