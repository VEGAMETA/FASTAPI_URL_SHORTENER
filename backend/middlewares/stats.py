from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


class StatsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Custom"] = "Example"
        return response