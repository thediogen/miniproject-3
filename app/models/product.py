import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from app.models.base import Base
from app.api.dependencies import Session_DP
from app.schemas import ProductSchema, DBProductSchema


class Product(Base):
    title: Mapped[str] = mapped_column(String(64))
    price: Mapped[int] = mapped_column()

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship('User', back_populates='products')

    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('orders.id', ondelete='SET NULL'), nullable=True)
    order = relationship('Order', back_populates='products')


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