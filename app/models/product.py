import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, ForeignKey

from app.models.base import Base
from app.schemas import DBProductSchema
from app.api.dependencies.db import Session_DP


class Product(Base):
    title: Mapped[str] = mapped_column(String(64))
    price: Mapped[int] = mapped_column()
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'))

    @classmethod
    async def create(cls, session: Session_DP, form_data: DBProductSchema):
        new = Product(
            title=form_data.title,
            price=form_data.price,
            user_id=form_data.user_id
        )

        session.add(new)
        await session.commit()

        return new
    