from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from time import ctime
from asyncio import sleep


async def sleeper(request):
    request_arrival_time = ctime()
    await sleep(10)
    request_delivery_time = ctime()
    return JSONResponse({
        "type": "sleeper",
        "arrival_time": request_arrival_time,
        "delivery_time": request_delivery_time,
    })


async def activer(request):
    request_arrival_time = ctime()
    request_delivery_time = ctime()
    return JSONResponse({
        "type": "activer",
        "arrival_time": request_arrival_time,
        "delivery_time": request_delivery_time,
    })


app = Starlette(debug=True, routes=[
    Route("/sleeper", sleeper),
    Route("/activer", activer),
])
