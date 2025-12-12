from fastapi import APIRouter, HTTPException, status
from app.core.database import get_master_db
from app.models.schemas import AdminLoginRequest, Token
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/admin", tags=["Authentication"])

@router.post("/login", response_model=Token)
async def login(login_data: AdminLoginRequest):
    db = get_master_db()
    
    # 1. Find the organization/admin by email in Master DB
    user = await db.organizations.find_one({"email": login_data.email})
    
    # 2. Check if user exists and password is correct
    if not user or not verify_password(login_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Create JWT Token
    access_token = create_access_token(
        subject=user["email"],
        claims={"org_id": user["organization_name"], "role": "admin"}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }