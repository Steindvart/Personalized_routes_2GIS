from pydantic import BaseModel

class UserBase(BaseModel):
  name: str
  email: str


class UserCreate(UserBase):
  password: str


class User(UserBase):
  id: int

  class Config:
    orm_mode = True


class CategoryBase(BaseModel):
  name: str


class Category(CategoryBase):
  id: int

  class Config:
    orm_mode = True


class FieldBase(BaseModel):
  name: str
  units: str


class Field(FieldBase):
  id: int

  class Config:
    orm_mode = True


class FieldValueBase(BaseModel):
  field_id: int
  value: str


class FieldValue(FieldValueBase):
  id: int

  class Config:
    orm_mode = True


class CategoryFieldBase(BaseModel):
  category_id: int
  field_id: int


class CategoryField(CategoryFieldBase):
  pass


class GlobalPreferenceBase(BaseModel):
  user_id: int
  category_id: int
  rating: float
  options: str


class GlobalPreference(GlobalPreferenceBase):
  id: int

  class Config:
    orm_mode = True
