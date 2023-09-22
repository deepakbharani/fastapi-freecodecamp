from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    email: EmailStr
    
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class SupplierBase(BaseModel):
    name: str
    address: str
    email: str
    phone: str
    vat_no: str

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    pass

class SupplierResponse(BaseModel):
    name: str
    address: str
    phone: str
    owner_id: int
    owner: UserOut
    # created_at: datetime

    class Config:
        orm_mode = True

class SupplierOut(BaseModel):
    Supplier: SupplierResponse
    Votes: int
    
    class Config:
        orm_mode = True
    
class Vote(BaseModel):
    supplier_id: int
    dir: conint(le=1)
