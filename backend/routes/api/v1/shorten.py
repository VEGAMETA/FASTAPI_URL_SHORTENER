import string
import random
from urllib.parse import urlparse

from fastapi import HTTPException
from sqlalchemy import select

from backend import api_v1_router, database
from backend.models import URL
from backend.schemas import URLShortenRequest


async def get_short_url(k: int = 4) -> str:
    """
    Generates a short URL
    if the URL already exists, it generates a new one
    """
    short_url = "".join(random.choices(string.ascii_letters + string.digits, k=k))
    query = select(URL).where(URL.short_url == short_url)
    db_url = await database.fetch_one(query)
    if db_url:
        return await get_short_url(k + 1)
    return short_url


@api_v1_router.post(
    "/shorten",
    responses={
        400: {"description": "URL too long"},
    },
    response_model=dict,
)
async def create_short_url(url_request: URLShortenRequest) -> dict:
    """
    Creates a short URL
    """
    original_url = url_request.url
    if len(original_url) > 524288:
        raise HTTPException(status_code=400, detail="URL too long")
    if not urlparse(original_url).scheme:
        original_url = urlparse(original_url)._replace(**{"scheme": "http"}).geturl()
    query = select(URL).where(URL.original_url == original_url)
    db_url = await database.fetch_one(query)
    if db_url:
        return {"short_url": db_url.short_url}
    short_url = await get_short_url()
    query = URL.__table__.insert().values(
        original_url=original_url,
        short_url=short_url,
    )
    await database.execute(query)
    return {"short_url": short_url}
