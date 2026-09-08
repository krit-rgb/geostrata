from fastapi import APIRouter, HTTPException, Request

from app.schemas.review_decision import ReviewDecision
from app.schemas.review_queue import ReviewQueueItem


router = APIRouter(prefix="/api/v1")


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/review-queue")
def get_review_queue(request: Request):
    workflow = request.app.state.review_workflow

    return {
        "items": [
            item.model_dump()
            for item in workflow.get_items()
        ]
    }


@router.post("/review-queue/{review_id}/decision")
def submit_review_decision(
    review_id: str,
    decision: ReviewDecision,
    request: Request,
):
    workflow = request.app.state.review_workflow

    item = workflow.get_item(review_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Review item not found",
        )

    reviewed_item = workflow.mark_reviewed(review_id)

    return {
        "review_id": review_id,
        "status": reviewed_item.status,
        "decision": decision.model_dump(),
    }