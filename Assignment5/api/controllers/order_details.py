from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create_order_detail(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        menu_item_id=order_detail.menu_item_id,
        quantity=order_detail.quantity,
        price=order_detail.price
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def read_all_order_details(db: Session):
    return db.query(models.OrderDetail).all()

def read_one_order_detail(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

def update_order_detail(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    update_data = order_detail.dict(exclude_unset=True)
    db_order_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_detail.first()

def delete_order_detail(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    db_order_detail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
