from fastapi import APIRouter, Request, Form

from app.models import Product, User
from app.api.dependencies import Session_DP, Auth_DP
from app.schemas import ProductSchema, DBProductSchema
from app.utils import make_response


products_r = APIRouter(tags=['products'])


@products_r.get('/get_products')
async def get_products(request: Request, session: Session_DP):
    products = await Product.all(session=session)

    return products


@products_r.post('/create_product')
async def create_product(request: Request, session: Session_DP, product: str = Form(...), token: str = Form(...)):
    print(product)
    product = ProductSchema.model_validate_json(product)

    user = await User.get(
        session=session, 
        column=User.token, 
        value=token
    )

    product = await Product.create(session=session, form_data=DBProductSchema(**product.model_dump(), user_id=user.id))
    product = make_response(product)

    return product

