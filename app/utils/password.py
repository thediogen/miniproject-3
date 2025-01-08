from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'])


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(provided_password: str, og_password: str):
    is_valid = pwd_context.verify(provided_password, og_password)

    return is_valid
