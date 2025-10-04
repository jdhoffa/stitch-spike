import pytest
from stitch_spike.routers.health import get_health


@pytest.mark.asyncio
async def test_get_health():
    response = await get_health()
    assert response.status == "OK"
