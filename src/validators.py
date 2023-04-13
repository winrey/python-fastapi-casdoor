from fastapi import HTTPException
from jwt import DecodeError
from .init import get_caseoor


def get_casdoor_if_ready(throw_http_exception: bool = True):
    casdoor = get_caseoor()
    if not casdoor:
        if throw_http_exception:
            raise HTTPException(status_code=500, detail="Casdoor is not boot")
        else:
            raise Exception("Casdoor is not boot")
    return casdoor



def validate_user_by_token(token: str, throw_http_exception: bool = True):
    casdoor = get_casdoor_if_ready(throw_http_exception)
    try:
        return casdoor.parse_jwt_token(token)
    except Exception as e:
        if not throw_http_exception:
            raise e
        if isinstance(e, DecodeError):
            raise HTTPException(status_code=401, detail="Invalid token")
        raise e
