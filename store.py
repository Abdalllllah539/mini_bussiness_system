from models import Product, Customer, Order
class Store:
    def __init__(self):
        self.Products = {}
        self.Customers = {}
        self.orders = {}
#########Products_Methods########################
    def add_product(self, product):
        if product.id in self.Products:
            return "Product ID already exists"
        self.Products[product.id] = product
        return "Product added successfully"
    
    def remove_product(self , product_id):
        if product_id not in self.Products.keys():
            return"Product ID Dosen't Exist"
        del self.Products[product_id] 
        
    def find_product(self, product_name):
        for product in self.Products.values():
            if product.name == product_name:
                return product.id
        return "Product not found"
    
    def display_products(self):
        a = 0
        for product in self.Products.values():
            print(f"{a+1}# {product}")
            a+=1

########################customer_methods############################
    def add_customer(self , customer):
        if customer.id in self.Customers:
            return "This Customer Alredy Existed"
        self.Customers[customer.id] = customer
        
    def remove_customer(self , customer_id):
        if customer_id not in self.Customers:
            return "This Customer Dosen't Exist in Our DataBase"
        del self.Customers[customer_id] 
        
    def find_customer(self, customer_name):
        for customer in self.Customers.values():
            if customer.name == customer_name:
                return f"ID: {customer.id}"
        return "This Customer Dosen't Exist in Our DataBase "
    
    def display_customers(self):
        a = 0
        for customer in self.Customers.values():
            print(f"{a + 1}# {customer.name}")
            a+=1
            
    def make_order(self):
        customer_id = input("What is the Customer ID?")
        if customer_id not in self.Customers.keys():
            print("This Customer Not In Our DataBase")
            return
        product_id = input("What is the Product ID?")
        if product_id not in self.Products.keys():
            print("This Product Not In The Store")
            return
        quantity = int(input("what is the Quantity?"))
        if quantity > self.Products[product_id].stock :
            print("This Quantity Not in The Stock")
            return
        total_price = quantity * self.Products[product_id].price
        print(f"Total Price-->{total_price:,}$")
        
        order_id = len(self.orders) + 1
        Order = order(
        order_id,
        customer_id,
        product_id,
        quantity,
        total_price
    )

        self.orders[order_id] = Order 
        self.Products[product_id].stock-=quantity 
            
                
        
        
        
        