from pydantic import BaseModel

class InputData(BaseModel):
    linkedin_job_post_title: str
    linkedin_job_post_description: str
    first_name: str
    last_name: str
    login_mail: str
    company_name: str
    skills: str | None = None
