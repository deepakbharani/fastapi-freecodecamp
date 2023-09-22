from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Supplier(Base):
    __tablename__ = "supplier_table"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String, nullable=False)
    vat_no = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users_table.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    
class User(Base):
    __tablename__ = "users_table"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users_table.id", ondelete="CASCADE"), primary_key=True)
    supplier_id = Column(Integer, ForeignKey("supplier_table.id", ondelete="CASCADE"), primary_key=True)