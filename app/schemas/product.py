import uuid

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    '''
    Such fields user should provide when creating new product
    '''

    title: str = Field(max_length=64)
    price: int = Field(gt=0)


class ProductResponseSchema(ProductSchema):
    id: int


class DBProductSchema(ProductSchema):
    '''
    In such form database receive new product to create it.
    '''

    user_id: uuid.UUID
