import random

from app.constants import ALL_SYMBOLS


def generate_token() -> str:
    token = ''

    for _ in range(32):
        token += ALL_SYMBOLS[random.randint(0, 66)]

    return token