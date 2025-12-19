from product import Product
class ProductMenager:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
    def list_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product)