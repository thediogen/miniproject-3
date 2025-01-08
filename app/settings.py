import os
from dotenv import load_dotenv

load_dotenv(override=True)


DB_CONFIG: str = (
    'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'.format(
        DB_USER=os.getenv('DB_USER'),
        DB_PASSWORD=os.getenv('DB_PASSWORD'),
        DB_HOST=os.getenv('DB_HOST'),
        DB_NAME=os.getenv('DB_NAME'),
        DB_PORT=os.getenv('DB_PORT')
    )
)

SESSION_MIDDLEWARE_SECRET_KEY: str = os.getenv('SESSION_MIDDLEWARE_SECRET_KEY')


# print(f'\n\n{DB_CONFIG}\n\n')
