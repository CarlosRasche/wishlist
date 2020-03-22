from aiohttp import web
from app.handlers.home_handler import handle
from app.handlers.add_product_handler import handle_add_product
from app.model.product_list import ProductList

app = web.Application()
app.add_routes([web.get("/", handle), web.get("/{name}", handle), web.post("/add_product", handle_add_product)])
app.product_list = ProductList(name="wishlist")


if __name__ == "__main__":
    print(app.product_list._name)
    web.run_app(app)
    print("app.name")
