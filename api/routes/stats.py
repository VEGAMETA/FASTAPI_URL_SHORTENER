from fastapi import HTTPException

from .base import *


@app.get(
    "/stats/{short_url}",
    responses={404: {"description": "URL not found"}},
    response_model=dict,
)
async def get_stats(short_url: str) -> dict:
    """
    Get stats for a short URL
    """
    db_url = await get_db_short_url(short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    redirect_count_query = select(StatURL).where(StatURL.url_id == db_url.id)
    redirect_count = await database.fetch_all(redirect_count_query)
    return {
        "redirect_count": len(redirect_count),
        "created_at": db_url.created_at,
        "last_redirected_at": (
            redirect_count[-1].redirected_at if redirect_count else None
        ),
    }
