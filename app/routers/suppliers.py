from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/suppliers",
    tags=['Suppliers']
)

# Get all the suppliers
#@router.get("/", response_model=List[schemas.SupplierResponse])
@router.get("/", response_model=List[schemas.SupplierOut])
async def get_suppliers(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), 
                        limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute(""" SELECT * FROM  supplier_table""")
    # suppliers = cursor.fetchall()
    # suppliers = db.query(models.Supplier).filter(models.Supplier.owner_id == current_user.id).all()
    
    suppliers = db.query(models.Supplier, func.count(models.Vote.supplier_id).label("Votes")).join(models.Vote, models.Supplier.id == models.Vote.supplier_id, isouter= True).group_by(models.Supplier.id).filter(models.Supplier.name.contains(search)).limit(limit).offset(skip).all()
    suppliers = list(map(lambda x:x._mapping,suppliers))

    return suppliers

# Create a new supplier
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.SupplierResponse)
async def create_supliers(supplier: schemas.SupplierCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO supplier_table (name, address, email, phone, vat_no, city, country) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING * """, (supplier.name, supplier.address, supplier.email, supplier.phone, supplier.vat_no, supplier.city, supplier.country))
    # new_supplier = cursor.fetchone()
    # conn.commit()
    # new_supplier = models.Supplier(name=supplier.name, address=supplier.address, email=supplier.email, phone=supplier.phone, vat_no=supplier.vat_no)

    new_supplier = models.Supplier(owner_id = current_user.id, **supplier.dict())
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)

    return new_supplier

# Get one supplier with id
@router.get("/{id}", response_model=schemas.SupplierOut)
def get_supplier_with_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM supplier_table WHERE id = %s """, (str(id),))
    # supplier_with_id = cursor.fetchone()

    #supplier_with_id = db.query(models.Supplier).filter(models.Supplier.id == id).first()

    supplier_with_id = db.query(models.Supplier, func.count(models.Vote.supplier_id).label("Votes")).join(
        models.Vote, models.Supplier.id == models.Vote.supplier_id, isouter= True).group_by(models.Supplier.id).filter(models.Supplier.id == id).first()

    if not supplier_with_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Supplier {id} was not found in here")
    
    if supplier_with_id.Supplier.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    return supplier_with_id

# Delete a supplier with id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier_with_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM supplier_table WHERE id = %s returning * """, (str(id),))
    # deleted_supplier_with_id = cursor.fetchone()
    # conn.commit()

    supplier_query = db.query(models.Supplier).filter(models.Supplier.id == id)
    supplier = supplier_query.first()

    if supplier_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Supplier with ID = {id} does not exist")
    
    if supplier.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    supplier_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schemas.SupplierResponse)
def update_supplier(id: int, updated_supplier: schemas.SupplierUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):   
    # cursor.execute("""UPDATE supplier_table SET name = %s, address = %s, email = %s, phone = %s, vat_no = %s, city = %s, country = %s WHERE id = %s RETURNING * """, (supplier.name, supplier.address, supplier.email, supplier.phone, supplier.vat_no, supplier.city, supplier.country, str(id),))
    # updated_supplier = cursor.fetchone()
    # conn.commit()
    
    supplier_query = db.query(models.Supplier).filter(models.Supplier.id == id)
    supplier = supplier_query.first()

    if supplier == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Supplier with ID = {id} does not exist")
    
    if supplier.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Not authorized to perform requested action")
    
    supplier_query.update(updated_supplier.dict(), synchronize_session=False)
    db.commit()

    return supplier_query.first()