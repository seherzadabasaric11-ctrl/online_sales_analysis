from product import Product
from product_menager import ProductMenager
def main():
    menager=ProductMenager()
    product1=Product("Laptop",1200,5)
    product2=Product("Phone",800,10)
    menager.add_product(product1)
    menager.add_product(product2)
    menager.list_products()
if __name__ == "__main__":
    main()