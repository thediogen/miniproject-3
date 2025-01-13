import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import BigInteger, String, Enum, ForeignKey
from decimal import Decimal

from app.models.base import Base


class Order(Base):
    total: Mapped[int] = mapped_column(BigInteger, nullable=True)

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship('User', back_populates='orders')

    products: Mapped[list['Product']] = relationship('Product', back_populates='order')
