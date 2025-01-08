from fastapi import Request, HTTPException, status

from app.api.dependencies.db import Session_DP
from app.models import User, Product
from app.schemas import ProductSchema, DBProductSchema


async def add_product(request: Request, 
                      session: Session_DP,
                      form_data: ProductSchema
):
    access_token = request.session.get('access_token')
    user = await User.get(session=session, column=User.token, value=access_token)
    user_id = user.id
    print(user_id)

    if user.role != 'seller':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='You cannot create products because you are not seller.'
        )

    form_data = DBProductSchema(**form_data.dict(), user_id=user_id)
    print(type(form_data), form_data)

    new_product = await Product.create(session=session, form_data=form_data)


    return new_product


async def get_products(request: Request,
                       session: Session_DP,
                       product_title: str
):
    '''
    Find and return all the matching products in database.
    '''

    products = await Product.all(session=session, column=Product.title, value=product_title)

    return products
