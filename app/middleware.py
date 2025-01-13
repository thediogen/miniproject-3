from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, status

from app.database import check_database_connection


async def DatabaseMiddleware(request: Request, call_next):

    db_connection_status = await check_database_connection()

    if db_connection_status == '\nWARNING: database is not connected\n':
        '''
        Якщо ДБ не підключена
        '''

        return 'NO'

        # raise HTTPException(
        #     status_code=status.HTTP_400_BAD_REQUEST,
        #     detail='This endpoint requires database connection, but database is not connected'
        # )
    
    response = await call_next(request)

    return response
    
