from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

# CRUD Operations for Sandwiches
def create_sandwich(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(
        name=sandwich.name,
        price=sandwich.price
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all_sandwiches(db: Session):
    return db.query(models.Sandwich).all()

def read_one_sandwich(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update_sandwich(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    update_data = sandwich.dict(exclude_unset=True)
    db_sandwich.update(update_data, synchronize_session=False)
    db.commit()
    return db_sandwich.first()

def delete_sandwich(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
