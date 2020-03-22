from aiohttp import web
from app.model.product_list import ProductList

async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = f'''Hello, this is the list {request.app.product_list._name}
{format_product_list(request.app.product_list._product_list)}'''
        
    return web.Response(text=text)


def format_product_list(product_list: ProductList) -> str:
    text = ""
    for product in product_list:
        text += f"{product.name} - {product.score}\n"
    return text