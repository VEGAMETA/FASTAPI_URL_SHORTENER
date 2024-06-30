from fastapi import HTTPException
from fastapi.responses import RedirectResponse

from .base import *


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
    db_url = await get_db_short_url(short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    click_query = StatURL.__table__.insert().values(url_id=db_url.id)
    await database.execute(click_query)
    return RedirectResponse(db_url.original_url, status_code=308)
