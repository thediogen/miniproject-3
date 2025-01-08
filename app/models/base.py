import uuid

from sqlalchemy import BigInteger, select, Uuid
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

from app.api.dependencies.db import Session_DP


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'
    
    # Queries

    @classmethod
    async def all(cls, session: Session_DP, column=None, value=None):
        stmt = None
        if column and value:
            stmt = select(cls).where(column == value)
        else:
            stmt = select(cls)
        query = await session.execute(stmt)
        
        result = query.scalars().all()

        return result
    
    @classmethod
    async def get(cls, session: Session_DP, column, value):
        '''
        Find and return first matching element in database.
        '''

        stmt = select(cls).where(column == value)
        query = await session.execute(stmt)
        result = query.scalars().first()

        return result