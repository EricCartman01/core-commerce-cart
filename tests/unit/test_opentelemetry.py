import pytest
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from src.resources.telemetry import (
    DatadogExporter,
    Exporter,
    FastAPIInstrument,
)


@pytest.mark.asyncio
async def test_should_instance_fastapi_app(app):
    assert isinstance(app, FastAPI)


@pytest.mark.asyncio
async def test_should_return_instance_exporter():
    assert isinstance(DatadogExporter(), Exporter)


@pytest.mark.asyncio
async def test_should_instrument_app_by_opentelemetry(app):
    FastAPIInstrument.perform_instrumentation(app)
    assert app._is_instrumented_by_opentelemetry
    assert FastAPIInstrumentor.is_instrumented_by_opentelemetry
