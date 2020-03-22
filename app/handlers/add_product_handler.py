from aiohttp import web


async def handle_add_product(request):
    text = "peepeepoopoo"
    payload = await request.json()
    print(payload)
    request.app.product_list.add_product(product_name = payload["name"], product_score = payload["score"])
    return web.Response(text=text)