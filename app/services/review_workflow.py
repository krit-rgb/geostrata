from app.schemas.review_queue import ReviewQueueItem


class ReviewWorkflow:
    def __init__(self):
        self.items: list[ReviewQueueItem] = []

    def add_item(self, item: ReviewQueueItem) -> ReviewQueueItem:
        self.items.append(item)
        return item

    def get_items(self) -> list[ReviewQueueItem]:
        return self.items

    def get_item(self, review_id: str) -> ReviewQueueItem | None:
        for item in self.items:
            if item.id == review_id:
                return item

        return None

    def mark_reviewed(self, review_id: str) -> ReviewQueueItem | None:
        item = self.get_item(review_id)

        if item is None:
            return None

        item.status = "reviewed"
        return item