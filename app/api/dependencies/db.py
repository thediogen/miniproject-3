from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.database import get_db_session


Session_DP = Annotated[AsyncSession, Depends(get_db_session)]