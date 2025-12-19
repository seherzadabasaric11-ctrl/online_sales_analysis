from product import Product
from product_menager import ProductMenager
from cart import Cart
def main():
    menager=ProductMenager()
    product1=Product(1,"Laptop Pro","Electronics",1200,3)
    product2=Product(2,"Smartphone","Electronics",900,8)
    menager.add_product(product1)
    menager.add_product(product2)
    menager.list_products()

    menager.remove_product("Phone")
    menager.list_products()
    
    cart=Cart()
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.show_cart()
    print("Total cart value: ",cart.total_price())
    cart.remove_from_cart("Laptop")
    cart.show_cart()    
    
if __name__ == "__main__":
    main()
    