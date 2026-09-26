from models import Product , Customer
from store import Store

phone = Product("samsung" ,233, 29999 , "available")
#print(phone)
store = Store()
customer = Customer("Boda" , "78250139" , "boda@mail.com" , "010053996694")
print(store.add_product(phone))
store.display_products()