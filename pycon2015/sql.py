#!/usr/bin/env python
# coding=utf-8


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    vote = Column(Integer, default=0)


class DatabaseProduct(object):

    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def vote(self, name):
        product = self.session.query(Product).filter_by(name=name).first()
        if product:
            product.vote += 1
            self.session.commit()
