from fastapi import APIRouter, HTTPException

from app.mock_data.review_queue import MOCK_REVIEW_QUEUE
from app.schemas.review_decision import ReviewDecision


router = APIRouter(prefix="/api/v1")


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/review-queue")
def get_review_queue():
    return {
        "items": MOCK_REVIEW_QUEUE
    }


@router.post("/review-queue/{review_id}/decision")
def submit_review_decision(
    review_id: str,
    decision: ReviewDecision
):
    for item in MOCK_REVIEW_QUEUE:
        if item["id"] == review_id:
            item["status"] = "reviewed"

            return {
                "review_id": review_id,
                "status": "recorded",
                "decision": decision.model_dump()
            }

    raise HTTPException(
        status_code=404,
        detail="Review item not found"
    )