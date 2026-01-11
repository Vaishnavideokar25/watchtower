from datetime import datetime

MONITORED_PAGES = [
    {
        "id": 1,
        "url": "https://careers.google.com/jobs",
        "keywords": ["apply", "deadline", "intern"],
        "added_at": datetime.utcnow().isoformat()
    },
    {
        "id": 2,
        "url": "https://university.edu/scholarships",
        "keywords": ["registration", "deadline"],
        "added_at": datetime.utcnow().isoformat()
    }
]

ALERTS_DB = [
    {
        "title": "Website change detected",
        "priority": "HIGH",
        "date": "2026-01-10",
        "why": "An important update was detected.",
        "action": "Please review the update manually.",
        "url": "https://careers.google.com/jobs"
    },
    {
    "title": "Website updated",
        "priority": "MEDIUM",
        "date": "2026-01-11",
        "why": "An  update was detected.",
        "action": "Please review the update manually.",
        "url": "https://careers.google.com/jobs"
    }
]
