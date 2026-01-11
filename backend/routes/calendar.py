from fastapi import APIRouter

router = APIRouter()

@router.post("/add")
def add_to_calendar(title: str, date: str):
    return {
        "message": "Event added to calendar",
        "title": title,
        "date": date
    }
