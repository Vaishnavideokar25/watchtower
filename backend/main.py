import firebase  # initializes Firebase
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.monitor import router as monitor_router
from routes.alerts import router as alerts_router
from routes.calendar import router as calendar_router
from routes.auth import router as auth_router


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔥 VERY IMPORTANT – initialize Firebase FIRST
import firebase  

from routes.auth import router as auth_router
from routes.alerts import router as alerts_router
from routes.monitor import router as monitor_router

app = FastAPI()

# CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(alerts_router)
app.include_router(monitor_router)


app = FastAPI(title="WatchTower Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/auth")
app.include_router(monitor_router, prefix="/monitor")
app.include_router(alerts_router, prefix="/alerts")
app.include_router(auth_router)
@app.get("/")
def root():
    return {"message": "WatchTower backend running 🚀"}
