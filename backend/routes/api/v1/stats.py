from fastapi import HTTPException
from sqlalchemy import select

from backend import api_v1_router, database
from backend.models import URL, StatURL


@api_v1_router.get(
    "/stats/{short_url}",
    responses={404: {"description": "URL not found"}},
    response_model=dict,
)
async def get_stats(short_url: str) -> dict:
    """
    Get stats for a short URL
    """
    query = select(URL).where(URL.short_url == short_url)
    db_url = await database.fetch_one(query)
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
