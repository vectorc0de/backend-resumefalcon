from fastapi import APIRouter, Body
from src.models.job_data import InputData

jobs_router = APIRouter()

@jobs_router.put("/jobs")
async def update_job(job_data: InputData = Body(...)):
    return {"message": job_data.linkedin_job_post_title}
