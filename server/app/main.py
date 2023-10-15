import time
from datetime import datetime
from typing import Callable

from fastapi import FastAPI, Request

app = FastAPI(title="Tourbasales API")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/test")
async def lessons_handler():
    return {"test": True}
