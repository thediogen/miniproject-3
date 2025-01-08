from fastapi import Request, HTTPException, status, Depends


def check_user(request: Request):
    access_token = request.session.get('access_token')

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='you are not authorised. Try to authorise or create new account'
        )
    return access_token


Auth_DP = Depends(check_user)
