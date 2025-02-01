"""Application module."""
import uvicorn
from fastapi import FastAPI
#
from app import urls
from app.containers import Container



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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)