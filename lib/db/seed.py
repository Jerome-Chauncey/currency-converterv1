import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from lib.db.models import Currency, ExchangeRate, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine("sqlite:///converter.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



currencies = [
    {"code": "USD", "name": "US Dollar", "symbol": "$"},
    {"code": "JPY", "name": "Japanese Yen", "symbol": "¥"},
    {"code": "GBP", "name": "British Pound", "symbol": "£"},
    {"code": "KES", "name": "Kenyan Shilling", "symbol": "Ksh"},
    {"code": "EUR", "name": "Euro", "symbol": "€"}
]



for data in currencies:
    if not session.query(Currency).filter_by(code=data["code"]).first():
        currency = Currency(**data)
        session.add(currency)

session.commit()

base = session.query(Currency).filter_by(code="USD").first()
target = session.query(Currency).filter_by(code= "EUR").first()

exchange_rates = ExchangeRate(
    base_currency_id = base.id,
    target_currency_id = target.id,
    rate = 0.93,
    timestamp= datetime.utcnow()
)
session.add(exchange_rates)
session.commit()

session.close()

print("Seeded currencies & Exchange rates successful")