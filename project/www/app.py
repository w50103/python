#!/usr/bin/env python3
# -*- coding: utf8 -*-


import logging;

from aiohttp import web

logging.basicConfig(level=logging.INFO)


import asyncio,os,json,time



def index(request):
    return web.Response(body = '<h1> hello world</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)

    app.router.add_route('GET', '/',index)

    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1', 8986)
    logging.info('server started at http://127.0.0.1:8986...')

    return srv

loop = asyncio.get_event_loop()

loop.run_until_complete(init(loop))

loop.run_forever()