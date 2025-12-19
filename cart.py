class Cart:
    def __init__(self):
        self.items=[]
    def add_to_cart(self,product):
        self.items.append(product)
        print(f"Product ˙{product.name}˙added to cart.")
    def remove_from_cart(self,product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Product ˙{product_name}˙removed from cart.")
                return
            print(f"Product ˙{product_name}˙not found in cart.")
    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        for product in self.items:
            print(product) 
    def total_price(self):
        total=0
        for product in self.items:
            total+= product.price *product.quantity
            return total       
        