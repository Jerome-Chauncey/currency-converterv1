from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"
    id = Column(Integer, primary_key=True)
    code = Column(String(3), unique=True, nullable=False)
    name = Column(String, nullable=False)
    symbol = Column(String)

    base_rates = relationship(
        "ExchangeRate",
        foreign_keys="ExchangeRate.base_currency_id",
        back_populates="base_currency",
    )
    target_rates = relationship(
        "ExchangeRate",
        foreign_keys="ExchangeRate.target_currency_id",
        back_populates="target_currency",
    )


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"
    id = Column(Integer, primary_key=True)
    base_currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    target_currency_id = Column(Integer, ForeignKey("currencies.id"), nullable=False)
    rate = Column(DECIMAL(10, 6), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    base_currency = relationship(
        "Currency", foreign_keys=[base_currency_id], back_populates="base_rates"
    )
    target_currency = relationship(
        "Currency", foreign_keys=[target_currency_id], back_populates="target_rates"
    )
