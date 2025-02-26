import functools

import aioinject
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import create_session


class TestRepository:

    def __init__(self, session: AsyncSession):
        self._session = session

    async def running(self):
        print('ya test')

@functools.lru_cache
def create_container() -> aioinject.Container:
    container = aioinject.Container()

    # container.register(aioinject.Scoped(create_session))
    # container.register(aioinject.Scoped(TestRepository))
    container.register(aioinject.Object(42))

    return container