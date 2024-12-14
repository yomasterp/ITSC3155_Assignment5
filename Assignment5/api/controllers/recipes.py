from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        name=recipe.name,
        description=recipe.description
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def read_all_recipes(db: Session):
    return db.query(models.Recipe).all()

def read_one_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update_recipe(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    update_data = recipe.dict(exclude_unset=True)
    db_recipe.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipe.first()

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    db_recipe.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
