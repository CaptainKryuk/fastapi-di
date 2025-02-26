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
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(AioInjectMiddleware, container=container)



    @app.get("/")
    @inject
    async def root(number: Injected[int], test: Injected[test]) -> int:
        print(test)
        return number

    return app


if __name__ == "__main__":
    uvicorn.run("main_test_aio:create_app", factory=True, reload=True)