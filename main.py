from product import Product
from product_menager import ProductMenager
def main():
    menager=ProductMenager()
    product1=Product(1,"Laptop","Electronics",1200,5)
    product2=Product(2,"Phone","Electronics",800,10)
    menager.add_product(product1)
    menager.add_product(product2)
    menager.list_products()

    menager.remove_product("Phone")
    menager.list_products()
    
if __name__ == "__main__":
    main()