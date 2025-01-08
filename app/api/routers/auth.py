from fastapi import Depends, status, HTTPException, Request

from app.schemas import UserAuthenticateForm, UserAuthorizeForm, UserResponseSchema
from app.api.dependencies.db import Session_DP
from app.models import User
from app.utils import verify_password


async def authenticate(request: Request, 
                       session: Session_DP, 
                       form_data: UserAuthenticateForm = Depends()
):
    '''
    This endpoint takes values provided by user and if it is valid creates new account
    in database and add token into request.session .
    If such user already exists raises HTTPException (401_UNAUTHORIZED).
    '''

    user = await User.get(session=session, column=User.email, value=form_data.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email already exists'
        )

    user = await User.create(session=session, form_data=form_data)

    request.session['access_token'] = user.token

    return user


async def authorize(request: Request,
                    session: Session_DP,
                    form_data: UserAuthorizeForm = Depends()
):
    '''
    This endpoint takes values provided by user and if it is valid takes them
    token and add id to request.session (LSS Do authorization)
    If provided data is not valid raises HTTPException (401_UNAUTHORIZED)
    '''

    user = await User.get(session=session, column=User.email, value=form_data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Such user does not exists. Try to authenticate'
        )
    
    is_password_valid = verify_password(form_data.password, user.password)

    if is_password_valid == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is incorrect'
        )
    
    request.session['access_token'] = user.token
    
    return user


async def log_out(request: Request):
    access_token = request.session.get('access_token')

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authorized'
        )

    del request.session['access_token']

    return 'log out'