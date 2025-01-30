"""Application module."""

from fastapi import FastAPI
#
from .containers import Container
from . import urls


def create_app() -> FastAPI:
    container = Container()
    # container.config.giphy.api_key.from_env("GIPHY_API_KEY")

    db = container.db()
    db.create_database()

    app = FastAPI(
        docs_url="/docs",
    )
    app.container = container
    app.include_router(urls.router)
    return app


app = create_app()