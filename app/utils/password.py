from fastapi import HTTPException, status
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'])


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(provided_password: str, og_password: str):
    is_valid = pwd_context.verify(provided_password, og_password)

    if is_valid == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is not correct'
        )

    return is_valid
