from fastapi import APIRouter

role = APIRouter()

@role.get("/roles/")
def shop_root():
    return {"Hello": "World"}

@role.get("/bad")
def shop_bad():
    return {"shop": "bad"}