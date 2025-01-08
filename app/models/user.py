from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, Enum

from app.models.base import Base
from app.schemas import UserSchema
from app.api.dependencies.db import Session_DP
from app.utils import hash_password, generate_token


class User(Base):
    username: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(256), index=True, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(Enum('admin', 'user', 'seller', name='user_roles'), default='user')
    token: Mapped[str] = mapped_column(unique=True)

    orders: Mapped[list['Order']] = relationship('Order', back_populates='')

    @classmethod
    async def create(cls, session: Session_DP, form_data: UserSchema):
        new = User(
            username=form_data.username,
            email=form_data.email,
            password=hash_password(form_data.password),
            role=form_data.role,
            token=generate_token(),
            orders=[]
        )

        session.add(new)
        await session.commit()

        return new
