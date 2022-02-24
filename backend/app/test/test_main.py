from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_maze_bar():
    response = client.get("/maze/?width=5&height=5&type=bar")
    assert response.status_code == 200
    maze = response.json()["maze"]
    assert len(maze) == 5
    for mz in maze:
        assert len(mz) == 5
        for m in mz:
            assert type(m) == int
            assert m >= 0 and m <= 1
    
    response = client.get("/maze/?width=10&height=10&type=bar")
    assert response.status_code == 200
    maze = response.json()["maze"]
    assert len(maze) == 11
    for mz in maze:
        assert len(mz) == 11
        for m in mz:
            assert type(m) == int
            assert m >= 0 and m <= 1
    
    response = client.get("/maze/?width=4&height=4&type=bar")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "The width and height of the maze must be at least 5.",
    }
    
    response = client.get("/maze/?width=5&height=4&type=bar")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "The width and height of the maze must be at least 5.",
    }
    
    response = client.get("/maze/?width=4&height=5&type=bar")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "The width and height of the maze must be at least 5.",
    }

