from flask import make_response, abort
from config import db
from models import Product
from serializer import ProductSchema

def read():
    product = Product.query.first()
    
    product_schema = ProductSchema()
    data = product_schema.dump(product)
    return data