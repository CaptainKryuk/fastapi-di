from dependency_injector import containers, providers

from .services import SearchService
from .gyphi import GyphiClient


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["app.urls"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    giphy_client = providers.Factory(
        GyphiClient,
        api_key=config.giphy.api_key,
        timeout=config.giphy.request_timeout,
    )

    search_service = providers.Factory(
        SearchService,
        gyphi_client=giphy_client,
    )

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )