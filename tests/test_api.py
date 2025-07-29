from fastapi.testclient import TestClient
from src.api.server import app

client = TestClient(app)

def test_update_job():
    response = client.put(
        "/jobs",
        json={
            "linkedin_job_post_title": "Software Engineer",
            "linkedin_job_post_description": "Job description",
            "first_name": "John",
            "last_name": "Doe",
            "login_mail": "john.doe@example.com",
            "company_name": "Example Inc.",
            "skills": "Python, FastAPI"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Software Engineer"}
