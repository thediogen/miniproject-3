from fastapi import APIRouter, Request, Depends, HTTPException, status, Form

from app.models import User
from app.api.dependencies import Session_DP
from app.schemas import UserSchema, UserResponseSchema, UserAuthenticateForm
from app.utils import make_response, verify_password


auth_r = APIRouter(tags=['auth'])


@auth_r.get('/get_user')
async def get_user(request: Request, session: Session_DP):
    '''
    this endpoint checks, is user authorised. If not raises HTTPException. If True - return user name (from database)
    '''

    access_token = request.session.get('access_token')

    print('CHECKING')

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authenticated'
        )
    
    user = await User.get(
        session=session, 
        column=User.token, 
        value=access_token
    )

    print(user.username)

    return user.username


@auth_r.post('/registration', response_model=UserResponseSchema)
async def registration(request: Request, session: Session_DP, form_data: UserSchema = Depends()):
    user = await User.get(session=session, column=User.email, value=form_data.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email already exists'
        )

    user = await User.create(session=session, form_data=form_data)

    user = make_response(user)

    return user


@auth_r.post('/authenticate')
async def authenticate(request: Request, session: Session_DP, form_data: str = Form(...)):

    form_data = UserAuthenticateForm.model_validate_json(form_data)

    print(form_data.email)
    print(form_data.password)

    user = await User.get(session=session, column=User.email, value=form_data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email does not exists'
        )
    
    verify_password(form_data.password, user.password)

    request.session['access_token'] = user.token

    print(user.token)

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
