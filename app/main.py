import contextlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.config import DB_CONFIG, SESSION_MIDDLEWARE_KEY
from app.database import session_manager, check_database_connection
from app.api.routers import auth_r, products_r, page_r, users_r


def get_app() -> FastAPI:

    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI):
        session_manager.init(DB_CONFIG)
        db_connection_status = await check_database_connection()
        print(db_connection_status)

        yield
        await session_manager.close()


    app = FastAPI(title='Miniproject 3', lifespan=lifespan)

    app.add_middleware(SessionMiddleware, secret_key=SESSION_MIDDLEWARE_KEY, same_site='none')
    app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173'], allow_methods=['*'])
    
    app.include_router(auth_r)
    app.include_router(products_r)
    app.include_router(page_r)
    app.include_router(users_r)

    return app


app = get_app()
