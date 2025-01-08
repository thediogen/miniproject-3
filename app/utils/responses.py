from app.schemas import UserResponseSchema


# RESPONSE_MODELS = {
#     'User': UserResponseSchema
# }


def make_response(instance):
    data = {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

    print(data)

    return
