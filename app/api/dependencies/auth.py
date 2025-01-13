from typing import Annotated

from fastapi import Request, HTTPException, status, Depends, Form
from fastapi.security import OAuth2PasswordBearer


def check_user(request: Request):
    access_token = request.session.get('access_token')

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authenticated. Try to authenticate or create new account'
        )
    return access_token


Auth_DP = Depends(check_user)


class AuthenticateForm:
    def __init__(self,
                 email: Annotated[str, Form],
                 password: Annotated[str, Form]
    ):
        self.email = email
        self.password = password


oath2_schema = OAuth2PasswordBearer(tokenUrl='authenticate')
