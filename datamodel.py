from sqlalchemy import (create_engine, Column, Integer,
                        REAL)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging


engine = create_engine("sqlite:///weather.db", echo=False)
Session = sessionmaker(bind=engine)
sesn = Session()
Base = declarative_base()


class WeatherDb(Base):
    __tablename__ = 'DATA'

    id = Column(Integer, primary_key=True)
    datetime = Column(Integer)
    temperature = Column(REAL)
    humidity = Column(Integer)
    wind = Column(REAL)
    pressure = Column(Integer)


def init_DB():
    Base.metadata.create_all(engine)


def insertData(temperature, humidity, wind_speed, pressure, now):
    ts = int(now.timestamp())
    new_record = WeatherDb(datetime=ts, temperature=temperature, humidity=humidity,
                           wind=wind_speed, pressure=pressure)
    sesn.add(new_record)
    sesn.commit()


