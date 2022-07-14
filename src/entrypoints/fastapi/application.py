from pathlib import Path

from fastapi import FastAPI

from entrypoints.fastapi.enums import Environment
from resources.telemetry import DatadogExporter, FastAPIInstrument, Telemetry


APP_ROOT = Path(__file__).parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    # Telemetry
    if Environment.is_valid():
        Telemetry.init()
        Telemetry.configure_exporter(DatadogExporter())

    app = FastAPI(
        title="app",
        description="ShoppingCart API",
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
    )

    @app.on_event("startup")
    async def startup_event() -> None:
        # Instrumentation
        if Environment.is_valid():
            Telemetry.instrument(FastAPIInstrument(), app)

    @app.on_event("shutdown")
    async def shutdown_event() -> None:
        # Instrumentation
        if Environment.is_valid():
            Telemetry.uninstrument(FastAPIInstrument(), app)

    return app
