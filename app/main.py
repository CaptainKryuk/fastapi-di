# """Application module."""
# import contextlib
# from collections.abc import AsyncIterator
#
# import uvicorn
# from aioinject import inject, Injected
# from aioinject.ext.fastapi import AioInjectMiddleware
# from fastapi import FastAPI
# # from app import urls
# import aioinject
#
# container = aioinject.Container()
# container.register(aioinject.Object(42))
#
#
# # @contextlib.asynccontextmanager
# # async def lifespan(
# #     _: FastAPI,
# # ):
# #     async with aclosing(create_container()):
# #         yield
#
# @contextlib.asynccontextmanager
# async def lifespan(_: FastAPI) -> AsyncIterator[None]:
#     async with container:
#         yield
#
# def create_app() -> FastAPI:
#     # di_container = Container()
#     # container.config.giphy.api_key.from_env("GIPHY_API_KEY")
#
#     # db = di_container.db()
#     # db.create_database()
#
#     app = FastAPI(
#         docs_url="/docs",
#         lifespan=lifespan,
#     )
#     # app.container = di_container
#     app.add_middleware(AioInjectMiddleware, container=container)
#     # app.include_router(urls.router)
#
#     class testrepo:
#         def __init__(self):
#             pass
#
#         def run(self):
#             print(123)
#
#     @app.get("/testtest")
#     @inject
#     async def root(number: Injected[int]) -> int:
#         print(number)
#         return number
#
#     return app


# app = create_app()

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)










import contextlib
from collections.abc import AsyncIterator

import uvicorn
from fastapi import FastAPI

import aioinject
from aioinject import Injected
from aioinject.ext.fastapi import AioInjectMiddleware, inject


class test:
    def __init__(self):
        pass

    async def execute(self):
        print('execute')


container = aioinject.Container()
container.register(aioinject.Object(42))
container.register(aioinject.Scoped(test))



@contextlib.asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    async with container:
        yield


def create_app() -> FastAPI:
    app = FastAPI(docs_url='/docs', lifespan=lifespan)
    app.add_middleware(AioInjectMiddleware, container=container)


    @app.get("/")
    @inject
    async def root(number: Injected[int], test: Injected[test]) -> int:
        print(test)
        return number

    return app

app = create_app()


# if __name__ == "__main__":
#     uvicorn.run("main_test_aio:create_app", factory=True, reload=True)