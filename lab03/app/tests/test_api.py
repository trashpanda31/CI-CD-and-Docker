import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_sum():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/sum", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5
