from backend import app, api_v1_router

app.include_router(api_v1_router, tags=["API v1"])
