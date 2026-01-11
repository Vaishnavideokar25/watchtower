from fastapi import APIRouter
from storage import ALERTS_DB

router = APIRouter()

@router.get("/")
def get_alerts():
    return ALERTS_DB
from fastapi import APIRouter
from storage import ALERTS_DB

router = APIRouter()

@router.get("/")
def get_alerts():
    return ALERTS_DB

