from aiohttp import web
import asyncio

async def index(request):

    await asyncio.sleep(1)
    return web.Response(
            text='Done!\n')

app = web.Application()
app.add_routes([web.get('/', index)])

web.run_app(app, port=5000)
