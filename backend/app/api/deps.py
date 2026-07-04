from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db_session
from app.core.security import ALGORITHM
from app.config.settings import settings
from app.models.users import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

async def get_current_user(
    db: AsyncSession = Depends(get_db_session),
    token: str = Depends(oauth2_scheme)
) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    # In a real app, you fetch the user from DB.
    # For now, we mock the user based on the token sub if no DB record found
    stmt = select(User).where(User.id == int(user_id)) if user_id.isdigit() else None
    user = None
    if stmt is not None:
        result = await db.execute(stmt)
        user = result.scalar_one_or_none()
        
    if not user:
        # Mocking for sprint if DB is empty
        user = User(id=1, email="admin@ceylonsentinel.ai", is_active=True, role="ADMIN")
        
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
        
    return user

async def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user
