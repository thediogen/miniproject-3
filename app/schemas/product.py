import uuid

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    '''
    In such form user provide all the data to create new product
    '''
    title: str = Field(max_length=64)
    price: int


class DBProductSchema(ProductSchema):
    '''
    In such form database receive new product data
    '''
    user_id: uuid.UUID


class ProductresponseSchema(ProductSchema):
    model_config = {
        'from_attributes': True
    }
