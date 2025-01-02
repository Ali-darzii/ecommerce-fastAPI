from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from cores.config import get_app_settings
from api.api import router
from cores.events import create_start_app_handler, create_stop_app_handler


def create_app() -> FastAPI:
    settings = get_app_settings()
    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    application.include_router(router, prefix=settings.api_prefix)

    return application


app = create_app()