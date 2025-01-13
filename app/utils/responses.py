from app.schemas import UserResponseSchema, ProductresponseSchema


# прив'язую ORM моделі до pydantic-response схем
RESPONSE_MODELS = {
    'User': UserResponseSchema,
    'Product': ProductresponseSchema
}


def make_response(instance):
    '''
    Приймає об\'єкт в ORM вигляді, перетворює його в ту форму, в якій має повертатись
    '''
    response_model = RESPONSE_MODELS[instance.__class__.__name__]
    instance = response_model.model_validate(instance)

    return instance
