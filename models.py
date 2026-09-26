class Product:
    def __init__(self , name, id , price , stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    def display_info (self):
        return f"Product: {self.name}\nid: {self.id}\nprice: {self.price}\nstock: {self.stock}\n"
    def __str__(self):
        return self.display_info()
            
class Customer :
    def __init__(self , name , id , email , phone):
        self.name = name
        self.id = id
        self.email = email
        self.phone = phone
    def display_info(self):
        return f"name: {self.name}\nID: {self.id}\nEmail: {self.email}\nphone: {self.phone}\n"
    def __str__(self):
        return self.display_info()
    
    
    
    
class order:
    def __init__(self , order_id , customer_id , product_id , quantity , total_price):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
    def display_info(self):
        return f"Order-ID---> {self.order_id}\nCustomer-ID--->{self.customer_id}\nProduct-ID--->{self.product_id}\nQuantity-->{self.quantity}\nTotal-Price--->{self.total_price}"
    def __str__(self):
        return self.display_info()
    
        
        
        
