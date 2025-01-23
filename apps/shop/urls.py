from fastapi import APIRouter

shop = APIRouter()

@shop.get("/food")
def shop_root():
    return {"Hello": "World"}

@shop.get("/bad")
def shop_bad():
    return {"shop": "bad"}