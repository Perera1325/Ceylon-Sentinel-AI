import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_chat_endpoint_sse():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/chat?user_query=Test&session_id=123")
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]
        
        # Test that we get some chunks from the generator
        content = response.text
        assert "event: progress" in content
        assert "event: complete" in content
        assert "Coordinator" in content
