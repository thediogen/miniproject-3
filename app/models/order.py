from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import BigInteger, String, Enum, ForeignKey
from decimal import Decimal

from app.models.base import Base


class Order(Base):
    total: Mapped[int] = mapped_column(BigInteger, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship('User', back_populates='orders')

    order_items: Mapped[list['OrderItem']] = relationship('OrderItem', back_populates='order')
