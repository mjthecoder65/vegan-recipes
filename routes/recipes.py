from fastapi import APIRouter
from models.recipe import Recipe

router = APIRouter()


@router.get("/api/v1/recipes", tags=["Recipes"])
def get_recipes():
    return {"data": []}


@router.get("/api/v1/recipes/{id}", tags=["Recipes"])
def get_recipe(id: int):
    return {}


@router.post("/api/v1/recipes")
def add_recipe(recipe: Recipe):
    return {}


@router.put("/api/v1/recipes/{id}")
def update_recipe(id: int):
    return {}


@router.delete("/api/v1/recipes/{id}")
def delete_recipe(id: int):
    return {}
