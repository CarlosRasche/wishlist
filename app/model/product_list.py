from typing import List

from product import Product


class ProductList:
    def __init__(self, name: str, product_list: List[Product] = None):
        self.name = name
        self.product_list = product_list if product_list is not None else []

    def add_product(self, product_name: str, product_score: int) -> None:
        prod1 = Product(name=product_name, score=product_score)
        self.product_list.append(prod1)


if __name__ == "__main__":
    print("hola")
    plist = ProductList(name="pl1")
    print(plist.name)
    plist.add_product(product_name="firstprod", product_score=8)
    plist.add_product(product_name="guac", product_score=4)
    print([f"{product.name} --- {product.score}" for product in plist.product_list])
