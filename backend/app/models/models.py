from ..db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    units = Column(String)


class FieldValue(Base):
    __tablename__ = "fields_values"

    id = Column(Integer, primary_key=True, index=True)
    field_id = Column(Integer, ForeignKey("fields.id"))
    value = Column(String)


class CategoryField(Base):
    __tablename__ = "categories_fields"

    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    field_id = Column(Integer, ForeignKey("fields.id"), primary_key=True)


class Preference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    rating = Column(DECIMAL(8, 2))
    options = Column(String)
