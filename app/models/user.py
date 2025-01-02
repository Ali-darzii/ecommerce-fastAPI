from sqlalchemy.orm import Mapped, mapped_column
from models import Base
from sqlalchemy import DateTime, String

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    phone_no: Mapped[str] = mapped_column(String(11),unique=True, index=True)
    password: Mapped[str] = mapped_column(String(128),index=True)
    last_login: Mapped[DateTime] = mapped_column(DateTime)
    is_active: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
