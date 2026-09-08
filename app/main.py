from fastapi import FastAPI

from app.api.routes import router
from app.schemas.review_queue import ReviewQueueItem
from app.services.review_workflow import ReviewWorkflow
from app.db.database import Base, engine
from app.db import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="3D ULPIN API",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Geostrata3D API is running!"}

review_workflow = ReviewWorkflow()

review_workflow.add_item(
    ReviewQueueItem(
        id="REVIEW-001",
        discrepancy_report_id="REPORT-001",
        status="pending",
    )
)

app.state.review_workflow = review_workflow

app.include_router(router)