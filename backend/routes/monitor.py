from fastapi import APIRouter, Form
from gemini import analyze_change
from storage import MONITORED_PAGES, ALERTS_DB
from datetime import datetime

router = APIRouter()

@router.get("/")
def get_pages():
    return MONITORED_PAGES


@router.post("/add")
def add_page(
    url: str = Form(...),
    uid: str = Form(...),
    keywords: str = Form(...)
):
    keyword_list = [k.strip() for k in keywords.split(",")]

    # Simulated AI detection
    ai = analyze_change(f"Change detected on {url}")

    page = {
        "url": url,
        "keywords": keyword_list,
        "uid": uid,
        "added_at": datetime.now().isoformat()
    }

    alert = {
        "title": "Website change detected",
        "priority": "HIGH",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "why": ai["why"],
        "action": ai["action"],
        "url": url
    }

    MONITORED_PAGES.append(page)
    ALERTS_DB.append(alert)

    return {
        "message": "Page added successfully",
        "page": page,
        "alert": alert
    }
from fastapi import APIRouter, Body
@router.post("/remove")
def remove_page(data: dict = Body(...)):
    url = data.get("url")

    if not url:
        return {"error": "URL missing"}

    # remove page
    MONITORED_PAGES[:] = [p for p in MONITORED_PAGES if p["url"] != url]

    # remove related alerts
    ALERTS_DB[:] = [a for a in ALERTS_DB if a.get("url") != url]

    return {"message": "Monitoring stopped permanently"}
