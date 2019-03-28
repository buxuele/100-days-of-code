# when: 2019/03/25 8:13 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

from aiohttp import web


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = "hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get("/{name}", handle)])

web.run_app(app)



