
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .context import current_user_context
from .validators import validate_user_by_token
from .models import User


security = HTTPBearer()


async def get_current_user_or_none_without_check(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    if credentials.scheme != "Bearer":
        return None
    token = credentials.credentials
    user_dict = validate_user_by_token(token)
    if not user_dict:
        return None
    user = User.from_token_dict(user_dict)
    current_user_context.set(user)
    return user


async def get_current_user_without_check(user: Annotated[User | None, Depends(get_current_user_or_none_without_check)]):
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user


async def get_current_user(user: Annotated[User, Depends(get_current_user_without_check)]):
    if user.isDeleted or user.isForbidden:
        raise HTTPException(status_code=403, detail="You are not allowed to login.")
    return user


async def need_admin_user(user: Annotated[User, Depends(get_current_user)]):
    if not user.isAdmin:
        raise HTTPException(status_code=403, detail="You are not the admin")
    return user
