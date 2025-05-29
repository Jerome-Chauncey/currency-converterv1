import sys
import os
import random
from datetime import datetime

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from lib.db.models import Currency, ExchangeRate, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///converter.db")


def seed_db():
    print("Dropping existing tables...")
    Base.metadata.drop_all(engine)

    print("Creating tables...")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    currencies = [
        {"code": "USD", "name": "US Dollar", "symbol": "$"},
        {"code": "EUR", "name": "Euro", "symbol": "€"},
        {"code": "KES", "name": "Kenyan Shilling", "symbol": "Ksh"},
        {"code": "USH", "name": "Ugandan Shilling", "symbol": "USh"},
        {"code": "RWF", "name": "Rwandan Franc", "symbol": "RF"},
        {"code": "TZS", "name": "Tanzanian Shilling", "symbol": "TSh"},
        {"code": "NGN", "name": "Nigerian Naira", "symbol": "₦"},
        {"code": "ZAR", "name": "South African Rand", "symbol": "R"},
        {"code": "EGP", "name": "Egyptian Pound", "symbol": "E£"},
        {"code": "GHS", "name": "Ghanaian Cedi", "symbol": "₵"},
        {"code": "XOF", "name": "West African CFA Franc", "symbol": "CFA"},
        {"code": "XAF", "name": "Central African CFA Franc", "symbol": "FCFA"},
        {"code": "BWP", "name": "Botswana Pula", "symbol": "P"},
        {"code": "DJF", "name": "Djiboutian Franc", "symbol": "Fdj"},
        {"code": "JPY", "name": "Japanese Yen", "symbol": "¥"},
        {"code": "GBP", "name": "British Pound", "symbol": "£"},
        {"code": "CAD", "name": "Canadian Dollar", "symbol": "C$"},
        {"code": "AUD", "name": "Australian Dollar", "symbol": "A$"},
        {"code": "INR", "name": "Indian Rupee", "symbol": "₹"},
        {"code": "CNY", "name": "Chinese Yuan", "symbol": "¥"},
        {"code": "BRL", "name": "Brazilian Real", "symbol": "R$"},
        {"code": "MXN", "name": "Mexican Peso", "symbol": "$"},
        {"code": "CHF", "name": "Swiss Franc", "symbol": "Fr"},
        {"code": "SEK", "name": "Swedish Krona", "symbol": "kr"},
        {"code": "NOK", "name": "Norwegian Krone", "symbol": "kr"},
    ]

    print("Seeding currencies...")
    for data in currencies:
        # Avoid duplicates just in case
        if not session.query(Currency).filter_by(code=data["code"]).first():
            currency = Currency(**data)
            session.add(currency)

    session.commit()
    print("Currencies seeded.")

    # Map code to currency objects
    code_to_currency = {currency.code: currency for currency in session.query(Currency).all()}

    print("Generating exchange rates for currency pairs...")
    exchange_rates = []
    for base_code in code_to_currency:
        for target_code in code_to_currency:
            if base_code != target_code:
                rate = round(random.uniform(0.01, 200), 4)
                exchange_rates.append(
                    ExchangeRate(
                        base_currency_id=code_to_currency[base_code].id,
                        target_currency_id=code_to_currency[target_code].id,
                        rate=rate,
                        timestamp=datetime.utcnow(),
                    )
                )

    session.bulk_save_objects(exchange_rates)
    session.commit()
    print(f"Seeded {len(exchange_rates)} exchange rates successfully.")

    session.close()
    print("Database seeding complete.")


if __name__ == "__main__":
    seed_db()
