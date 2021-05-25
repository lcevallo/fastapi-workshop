import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    data = sa.Column(sa.Date)
    kind = sa.Column(sa.String(255))
    amount = sa.Column(sa.Numeric(10, 2))
    description = sa.Column(sa.Text, nullable=True)
