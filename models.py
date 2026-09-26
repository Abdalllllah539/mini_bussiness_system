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
    
        
        
        
