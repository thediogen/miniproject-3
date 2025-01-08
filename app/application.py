from io import BytesIO
import contextlib

from PIL import Image
from fastapi import FastAPI, UploadFile, APIRouter
from starlette.responses import StreamingResponse
from starlette.middleware.sessions import SessionMiddleware

from app.api.dependencies.auth import Auth_DP

from app.api.routers.users import get_all_users
from app.api.routers.products import add_product, get_products
from app.api.routers.auth import authenticate, authorize, log_out
from app.database import session_manager, check_database_connection
from app.settings import DB_CONFIG, SESSION_MIDDLEWARE_SECRET_KEY


def get_application(DB_CONFIG: str) -> FastAPI:

    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI):
        session_manager.init(DB_CONFIG)
        await check_database_connection()

        yield
        await session_manager.close()


    app = FastAPI(lifespan=lifespan)    

    app.add_middleware(SessionMiddleware, secret_key=SESSION_MIDDLEWARE_SECRET_KEY)

    app.add_api_route('/authenticate', authenticate, tags=['auth'], methods=['POST'])
    app.add_api_route('/authorize', authorize, tags=['auth'], methods=['POST'])
    app.add_api_route('/log_out', log_out, tags=['auth'], methods=['POST'])

    app.add_api_route('/products', add_product, tags=['products'], dependencies=[Auth_DP], methods=['POST'])
    app.add_api_route('/products', get_products, tags=['products'], dependencies=[Auth_DP], methods=['GET'])

    return app


app = get_application(DB_CONFIG=DB_CONFIG)


# app.add_api_route('/users', tags=['users'], endpoint=get_all_users)


# @app.post('/')
# async def upload_file(file: UploadFile):
#     data = await file.read()
#     # img = Image.frombytes('RGBA', (400, 400), data)
#     image_stream = BytesIO(data)

#     print(img)