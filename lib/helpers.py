from lib.db.models import Currency, ExchangeRate
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///converter.db")
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("👋 Goodbye!")
    exit()

def convert_currency():
    print("💱 Convert your money!")

    currencies = session.query(Currency).all()
    if not currencies:
        print("No currencies found.")
        return
    
    try:
        amount = float(input("Enter the amount to convert: "))

        print("\nAvaliable currencies:")
        for idx, c in enumerate(currencies, start=1):
            print(f"{idx}. {c.code} ({c.name})")

        base_idx = int(input("Choose the number of the currency you're converting FROM: ")) -1
        target_idx = int(input("Choose the number of the currency you're converting TO: ")) -1

        base = currencies[base_idx]
        target = currencies[target_idx]

        if base.id == target.id:
            print("You chose the same currency.")
            return
        
        rate_obj = session.query(ExchangeRate).filter_by(
            base_currency_id = base.id
            target_currency_id=target.id
        ).order_by(ExchangeRate.timestamp.desc()).first()

        if not rate_obj:
            print("Exchange rate not found.")
            return
        
        converted = float(rate_obj.rate) * amount
        print(f"Converted amount: {target.symbol}{converted:,.2f}")
    except Exception as e:
        print(f"Error: {e}")


def list_currencies():
    currencies = session.query(Currency).all()
    if currencies:
        for c in currencies:
            print(f"{c.code} - {c.name} ({c.symbol})")
    else:
        print("No currencies found.")

def find_currency_by_code():
    code = input("Enter currency code (e.g., USD): ").upper()
    currency = session.query(Currency).filter_by(code=code).first()
    if currency:
        print(f"Found: {currency.code} - {currency.name} ({currency.symbol})")
    else:
        print("Currency not found.")

def create_currency():
    code = input("Currency code: ").upper()
    name = input("Currency name: ")
    symbol = input("Currency symbol: ")

    try:
        new_currency = Currency(code=code, name=name, symbol=symbol)
        session.add(new_currency)
        session.commit()
        print(f"Created: {new_currency}")
    except Exception as e:
        session.rollback()
        print("Error creating currency: {e}")


def update_currency():
    code = input("Enter currency code to update: ").upper()
    currency = session.query(Currency).filter_by(code=code).first()
    if currency:
        currency.name = input(f"New name for {code} (current: {currency.name}): ")
        currency.symbol = input(f"New symbol for {code} (current: {currency.symbol}): ")
        try:
            session.commit()
            print(f"Updated: {currency}")
        except Exception as e:
            session.rollback()
            print(f"Error updating: {e}")
    else:
        print("Currency not found.")

def delete_currency():
    code = input("Enter currency code to delete: ").upper()
    currency = session.query(Currency).filter_by(code=code).first()
    if currency:
        confirm = input(f"Are you sure you want to delete {currency.code}? (y/n): ").lower()
        if confirm == "y":
            try:
                session.delete(currency)
                session.commit()
                print("Deleted.")
            except Exception as e:
                session.rollback()
                print(f"Error deleting: {e}")
    else:
        print("Currency not found.")






















































# from lib.db.models import Currency, ExchangeRate
# from sqlalchemy.orm import Session

# def convert_currency(amount: float, rate: float) -> float:
#     """convert amount using the given the exchange rate."""
#     return round(amount * rate, 2)

# def get_currency_by_code(session: Session, code: str) -> Currency:
#     """Fetch a currency by its code (case-insensitive)."""
#     return session.query(Currency).filter_by(code=code.upper()).first()

# def list_all_currencies(session: Session):
#     """Return all currencies in the database."""
#     return session.query(Currency).all()

# def get_exchange_rate(session: Session, base_code: str, target_code: str) -> ExchangeRate:
#     """Get the latest exchange rate between two currencies."""

#     base = get_currency_by_code(session, base_code)
#     target = get_currency_by_code(session, target_code)


#     if not base or not target:
#         return None
    
#     return session.query(ExchangeRate).filter_by(
#         base_currency_id=base.id,
#         target_currency_id=target.id
#     ).order_by(ExchangeRate.timestamp.desc()).first()