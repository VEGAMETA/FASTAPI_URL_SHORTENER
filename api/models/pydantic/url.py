from pydantic import BaseModel, Field


class URLShortenRequest(BaseModel):
    url: str = Field(default=None, description="Enter original url")
