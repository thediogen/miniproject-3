from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import BigInteger, String, Enum, ForeignKey
from decimal import Decimal

from app.models.base import Base


class OrderItem(Base):
    __tablename__ = 'order_items'

    total: Mapped[int] = mapped_column(BigInteger, nullable=True)
    quantity: Mapped[int] = mapped_column(BigInteger, default=1)

    product_id = mapped_column(ForeignKey('products.id'))
    products: Mapped['Product'] = relationship('Product')

    order_id = mapped_column(ForeignKey('orders.id'))
    order: Mapped['Order'] = relationship('Order', back_populates='')
