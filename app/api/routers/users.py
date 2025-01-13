from fastapi import APIRouter, Request

from app.models import User
from app.api.dependencies import  Auth_DP


users_r = APIRouter(tags=['users'], dependencies=[Auth_DP])


@users_r.get('/users')
async def main(request: Request):
    return {'response': 200}
