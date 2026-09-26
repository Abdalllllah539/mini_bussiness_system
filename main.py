from models import Product , Customer
from store import Store

phone = Product("samsung" ,"233", 29999 , 3000)
#print(phone)
store = Store()
store.add_product(phone)
customer = Customer("Boda" , "1" , "boda@mail.com" , "010053996694")
store.add_customer(customer)
#store.make_order()
print(store.Customers)
print(store.Products)


store.make_order()das