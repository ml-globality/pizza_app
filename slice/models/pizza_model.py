"""
Pizza Model

"""
from microcosm_postgres.models import EntityMixin, Model
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Pizza(EntityMixin, Model):
    """
    Defines a Pizza Object.

    """
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True)
    toppings = relationship("Topping")


