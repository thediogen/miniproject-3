from fastapi import APIRouter, Request

from app.models import Product, User
from app.api.dependencies import Session_DP, Auth_DP
from app.schemas import ProductSchema, DBProductSchema
from app.utils import make_response


products_r = APIRouter(tags=['products'], dependencies=[Auth_DP])


# @products_r.get('/products')
# async def get_products(request: Request):



@products_r.post('/products')
async def create_product(request: Request, session: Session_DP, product: ProductSchema):
    user = await User.get(
        session=session, 
        column=User.token, 
        value=request.session.get('access_token')
    )

    product = await Product.create(session=session, form_data=DBProductSchema(**product.model_dump(), user_id=user.id))
    product = make_response(product)

    return product

