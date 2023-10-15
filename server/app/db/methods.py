from db.base import session
from services.cbr import get_currency_rate
from sqlalchemy import select
from sqlalchemy.orm import joinedload
