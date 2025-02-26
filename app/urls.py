
from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependency_injector.wiring import inject as di_inject, Provide
from starlette import status
from aioinject import inject, Injected

from app.aio_container import TestRepository
from app.repositories import NotFoundError
from .services import UserService
from .di_container import Container


class Gif(BaseModel):
    url: str


class Response(BaseModel):
    query: str
    limit: int
    gifs: List[Gif]


router = APIRouter()


@router.get("/users")
@di_inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()


@router.get("/users/{user_id}")
@di_inject
def get_by_id(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
@di_inject
def add(
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user()


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@di_inject
def remove(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.get(
#     "/status",
#     response_model=dict,
# )
# # @aio_di_inject
# async def get_status(
#     # repository: Injected[TestRepository],
#     repository: TestRepository = None,
# ) -> dict:
#     print(repository)
#     return {'status': 'ok'}

@router.get(
    "/status",
)
@inject
def get_status(
    repo: Injected[int],
) -> None:
    print(repo)
    return 'ok'
