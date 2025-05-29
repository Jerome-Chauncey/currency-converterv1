from lib.db.models import Currency, ExchangeRate
from sqlalchemy.orm import Session

def convert_currency(amount: float, rate: float) -> float:
    """convert amount using the given the exchange rate."""
    return round(amount * rate, 2)

def get_currency_by_code(session: Session, code: str) -> Currency:
    """Fetch a currency by its code (case-insensitive)."""
    return session.query(Currency).filter_by(code=code.upper()).first()

def list_all_currencies(session: Session):
    """Return all currencies in the database."""
    return session.query(Currency).all()

def get_exchange_rate(session: Session, base_code: str, target_code: str) -> ExchangeRate:
    """Get the latest exchange rate between two currencies."""

    base = get_currency_by_code(session, base_code)
    target = get_currency_by_code(session, target_code)


    if not base or not target:
        return None
    
    return session.query(ExchangeRate).filter_by(
        base_currency_id = base.id
        target_currency_id = target.id
    ).order_by(ExchangeRate.timestamp.desc()).first()