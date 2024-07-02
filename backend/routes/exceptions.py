from fastapi.responses import FileResponse
from backend import app


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return FileResponse("./frontend/templates/404.html")
