from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.api.deps import get_db_session, get_current_user
from app.core.security import create_access_token, verify_password
from app.config.settings import settings
from app.models.users import User
from pydantic import BaseModel

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    role: str

@router.post("/login", response_model=Token)
async def login_access_token(
    db: AsyncSession = Depends(get_db_session),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """OAuth2 compatible token login, get an access token for future requests."""
    # Note: In a real enterprise system, query DB. For mock sprint:
    stmt = select(User).where(User.email == form_data.username)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    # Mocking for the dashboard to allow admin@ceylonsentinel.ai
    if not user and form_data.username == "admin@ceylonsentinel.ai":
        user = User(id=1, email="admin@ceylonsentinel.ai", hashed_password="mock", is_active=True, role="ADMIN")
        # We bypass password check for the mock
    elif not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
        
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.get("/me", response_model=UserResponse)
def test_token(current_user: User = Depends(get_current_user)) -> Any:
    """Test access token."""
    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_active": current_user.is_active,
        "role": getattr(current_user, 'role', 'USER')
    }
