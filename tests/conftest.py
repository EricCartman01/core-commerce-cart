import pytest
from fastapi import FastAPI


@pytest.fixture()
def app() -> FastAPI:
    from src.entrypoints.fastapi.application import get_app

    app = get_app()
    return app
