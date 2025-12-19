class Product:
    def __init__(self,product_id,name,category,price,quantity):
        self.product_id=product_id
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
        
    def __str__(self):
        return(f"ID:{self.product_id}, "
               f"Name:{self.name}, "
               f"Category:{self.category}, "
               f"Price:{self.price}, "
               f"Quantity:{self.quantity}, ")
        