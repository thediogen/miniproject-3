from fastapi import APIRouter, Request, Depends, HTTPException, status, Form
from pydantic import ValidationError

from app.models import User
from app.api.dependencies import Session_DP
from app.schemas import UserSchema, UserResponseSchema, UserAuthenticateForm
from app.utils import make_response, verify_password


auth_r = APIRouter(tags=['auth'])


@auth_r.post('/get_user')
async def get_user(request: Request, session: Session_DP, token: str = Form(...)):
    '''
    this endpoint checks, is user authorised. If not raises HTTPException. If True - return user name (from database)
    '''

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authenticated'
        )
    
    user = await User.get(
        session=session, 
        column=User.token, 
        value=token
    )

    return {
        'username': user.username,
        'user_role': user.role
    }


@auth_r.post('/registration')
async def registration(request: Request, session: Session_DP, form_data: str = Form()):

    try:
        form_data = UserSchema.model_validate_json(form_data)
    except ValidationError as er:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email or password is incorrect'
        )

    user = await User.get(session=session, column=User.email, value=form_data.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email already exists'
        )

    user = await User.create(session=session, form_data=form_data)

    # user = make_response(user)

    return user.token


@auth_r.post('/authenticate')
async def authenticate(request: Request, session: Session_DP, form_data: str = Form(...)):
    print(form_data)

    try:
        form_data = UserAuthenticateForm.model_validate_json(form_data)
    except ValidationError as er:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email or password is incorrect'
        )

    user = await User.get(session=session, column=User.email, value=form_data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email does not exists'
        )
    
    verify_password(form_data.password, user.password)

    request.session['access_token'] = user.token

    return {
        'access_token': user.token
    }


@auth_r.post('/log_out')
async def log_out(request: Request, session: Session_DP):
    access_token = request.session.get('access_token')

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authenticated'
        )
    
    del request.session['access_token']

    return {
        'status': 200,
        'detail': 'logged out'
    }
