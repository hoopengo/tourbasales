import uuid

from db._enums import OrderStatus
from db.base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import UUID
from sqlalchemy.types import Enum as SQLAlchemyEnum
