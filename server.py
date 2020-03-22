from aiohttp import web
from app.model.product_list import ProductList


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = f'''Hello, this is the list {request.app.product_list._name}
{request.app.product_list._product_list}'''
        
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get("/", handle), web.get("/{name}", handle)])
app.product_list = ProductList(name="wishlist")


if __name__ == "__main__":
    print(app.product_list._name)
    web.run_app(app)
    print("app.name")
