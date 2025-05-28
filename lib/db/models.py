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

    @classmethod
    def create(cls, session, **kwargs):
        currency = cls(**kwargs)
        session.add(currency)
        session.commit()
        return currency

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, id_):
        return session.query(cls).filter_by(id=id_).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @property
    def uppercase_code(self):
        return self.code.upper()
    
    def __repr__(self):
        return f"<Currency {self.code} ({self.name})>"
    


    


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


    def create(cls, session, **kwargs):
        rate = cls(**kwargs)
        session.add(rate)
        session.commit()
        return rate
    
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, id_):
        return session.query(cls).filter_by(id=id_).first()
    
    def delete(self, session):
        session.delete(self)
        session.commit()

    @property
    def formatted_rate(self):
        return f"{float(self.rate):, .6f}"
    
    def __repr__(self):
        return f"Exchangerate {self.base_currency.code} to {self.target_currency.code} @ {self.formatted_rate}"
