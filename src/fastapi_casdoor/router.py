from fastapi import APIRouter, Depends

from . import deps, models

casdoor_router = APIRouter()

@casdoor_router.get('/me', tags=['casdoor'], response_model=models.User)
def route_get_current_user(user: models.User = Depends(deps.get_current_user)):
    return user
