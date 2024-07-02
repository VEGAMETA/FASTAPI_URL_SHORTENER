from fastapi.responses import FileResponse
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select

from backend import app, database
from backend.models import URL, StatURL
from backend.schemas import URLShortenRequest


@app.get("/")
async def index():
    return FileResponse("./frontend/templates/index.html")


@app.get("/stats")
async def stats():
    # if url:
    #     url.url
    return FileResponse("./frontend/templates/stats.html")


@app.get(
    "/{short_url}",
    responses={
        404: {"description": "URL not found"},
        308: {"description": "URL has been redirected"},
    },
    response_class=RedirectResponse,
)
async def redirect_url(short_url: str) -> RedirectResponse:
    """
    Redirects to the original URL
    """
    query = select(URL).where(URL.short_url == short_url)
    db_url = await database.fetch_one(query)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    query = StatURL.__table__.insert().values(url_id=db_url.id)
    await database.execute(query)
    return RedirectResponse(db_url.original_url, status_code=307)
