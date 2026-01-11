from fastapi import APIRouter, HTTPException, Header
from firebase_admin import auth

router = APIRouter(prefix="/auth", tags=["Auth"])


# ===============================
# 🔐 VERIFY FIREBASE TOKEN
# ===============================
@router.post("/verify")
def verify_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        token = authorization.split(" ")[1]  # Bearer <token>
        decoded = auth.verify_id_token(token)

        return {
            "uid": decoded["uid"],
            "email": decoded.get("email")
        }

    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# ===============================
# ✍️ SIGNUP (OPTIONAL)
# ===============================
@router.post("/signup")
def signup(email: str, password: str):
    try:
        user = auth.create_user(email=email, password=password)
        return {
            "uid": user.uid,
            "email": user.email
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
