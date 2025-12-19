from product import Product
from product_menager import ProductMenager
def main():
    menager=ProductMenager()
    product1=Product(1,"Laptop Pro","Electronics",1200,3)
    product2=Product(2,"Smartphone","Electronics",900,8)
    menager.add_product(product1)
    menager.add_product(product2)
    menager.list_products()

    menager.remove_product("Phone")
    menager.list_products()
    
if __name__ == "__main__":
    main()