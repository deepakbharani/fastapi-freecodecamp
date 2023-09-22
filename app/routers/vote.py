from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/vote",
    tags=['Votes']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    vote_exists = db.query(models.Supplier).filter(models.Supplier.id == vote.supplier_id).first()

    if not vote_exists:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"the supplier with ID {vote.supplier_id} does not exits")

    vote_query = db.query(models.Vote).filter(models.Vote.supplier_id == vote.supplier_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = f"user {current_user.id} has already voted on supplier {vote.supplier_id}")
        
        new_vote = models.Vote(supplier_id = vote.supplier_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message": "successfully added a vote"}

    else:
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Vote does not exists")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message": "successfully deleted a vote"}