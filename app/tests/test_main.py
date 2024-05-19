from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_file():
    with open("C:/Nikhil/WallPaper.jpg", "rb") as file:
        response = client.post("/upload/", files={"file": file})
    assert response.status_code == 200
    assert "file_path" in response.json()

def test_get_nonexistent_file():
    response = client.get("/files/nonexistent_file.txt")
    assert response.status_code == 404
    assert "detail" in response.json()
