"""
Topping Model

"""
from microcosm_postgres.models import EntityMixin, Model
from sqlalchemy import Column, String, Integer


class Topping(EntityMixin, Model):
    """
    Defines a Topping Object.

    """
    __tablename__ = "toppings"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


    def __init__(self, name):
        self.name = name