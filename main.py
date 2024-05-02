import uvicorn
import json
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import redis_wrapper
from dotenv import dotenv_values
from ollama import Client
from enum import Enum

class LinkedinDats:
    def get_easy_apply(self):
        job_description = {
            "style": None,
            "js_path": None,
            "selector": ["#job-details > div"]
        }

        country = {
            "content": [],
            "style": [],
            "js_path": [],
            "selector": [],
            "optional": True,
            "order": 2
        }

        resume_load = {
            "is_button": True,
            "text": "upload resume",
            "order": 4,
            "optional": True,
            "selector": ["#ember$$$ > div > div > form > div > div:nth-child(2) > div > div > div > label > span",
                         "#ember$$$ > div > div:nth-child(2) > form > div > div > div > div > div > label > span"]
        }

        email = {
        "content": [],
        "is_input": True,
        "style": None,
        "js_path": [],
        "selector": []
        }

        next_button2 = {
            "style": ["artdeco-button__text"],
            "text": "Next",
            "js_path": None,
            "is_button": True,
            "selector": None,
            "order": 6
        }

        mobile = {
            "content": "4129998866",
            "is_input": True,
            "order": 1,
            "is_pattern": True,
            "style": ["fb-dash-form-element__error-field artdeco-text-input--input",
                      " artdeco-text-input--input$$$",
                      "fb-dash-form-element__error-field artdeco-text-input--input",
                      "artdeco-text-input--input",
                      "fb-dash-form-element__error-field artdeco-text-input--input",
                      "fb-dash-form-element__error-field artdeco-text-input--input",
                      " artdeco-text-input--input$$$"],

            "js_path": None,
            "id": ["single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3812991222-111026299-phoneNumber-nationalNumber"],
            "selector": None,
            "optional": False
        }

        next_button = {
            "style": ["artdeco-button__text"],
            "text": "Next",
            "js_path": None,
            "is_button": True,
            "selector": None,
            "order": 3,
            "optional": True
        }

        resume_load_completed = {
            "js_path": ["#jobsDocumentCardToggleLabel-ember$$$"],
            "selector": ["#ember358"],
            "style": ["artdeco-button artdeco-button--2 artdeco-button--primary ember-view"],
            "is_pattern": True,
            "order": 5,
            "text": "submit",
            "optional": False
        }

        skills = {}

        job_title = {}

        return {
                "job": {
                    "description": job_description,
                    "skills": skills,
                    "job_title": job_title
                },

                "apply_job": {"email": email,
                              "next_button": next_button,
                              "country": country,
                              "next_button2": next_button2,
                              "mobile": mobile,
                              "resume_load_completed": resume_load_completed,
                              "resume_load": resume_load
                              }
                }

class PlatformId(Enum):
    DICE = 1
    LINKEDIN = 2
    MONSTER = 3
    INDEED = 5
    ZIPRECRUITER = 4


app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


class Html(BaseModel):
    site_flag: int
    content_raw: str


class InputData(BaseModel):
    linkedin_job_post_title: str
    linkedin_job_post_description: str
    first_name: str
    last_name: str
    login_mail: str
    company_name: str
    skills: str | None = None


@app.put("/jobs")
async def update_job(job_data: dict = Body(...)):
  """
  Recv un from easy apply.

  Parameters:
      job_data (dict): Diccionary

  Return:
      dict: string message
  """

  payload = job_data.get("payload", {})
  login_mail = payload.get("login_mail", "")
  linkedin_job_post_title = payload.get("linkedin_job_post_title", "")
  linkedin_job_post_description = payload.get("linkedin_job_post_description", "")
  company_name = payload.get("company_name", "")
  skills = payload.get("skills", "")
  easy_apply = job_data.get("linkedin", {}).get("easyApply", False)

  return {"message": linkedin_job_post_title}


def llama2_parser(response):
    first_name = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": "2222222",
        "js_path": "2222222",
        "selector": "111111"
    }

    second_name = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": "2222222",
        "js_path": "2222222",
        "selector": "111111"
    }

    mobile = {
        "content": "4129875687",
        "is_input": True,
        "order": 1,
        "optional": True,
        # "style": "artdeco-text-input--input",
        "style": " artdeco-text-input--input$$$",
        # "style": "fb-dash-form-element__error-field artdeco-text-input--input",
        # "style": "fb-dash-form-element__error-field artdeco-text-input--input",

        "js_path": None,
        "id": "single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3812991222-111026299-phoneNumber-nationalNumber",
        "selector": None
    }

    email = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": None,
        "js_path": "2222222",
        "selector": "111111"
    }

    address1 = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": "2222222",
        "js_path": "2222222",
        "selector": None
    }

    zip_code = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": "2222222",
        "js_path": "2222222",
        "selector": "111111"
    }

    state = {
        "content": "AAAAAAAA",
        "is_input": False,
        "style": None,
        "js_path": "2222222",
        "selector": "111111"
    }

    experience_details = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": "2222222",
        "js_path": None,
        "selector": "111111"
    }

    facebook = {
        "content": "AAAAAAAA",
        "is_input": False,
        "style": "2222222",
        "js_path": "2222222",
        "selector": "111111"
    }

    proposal = {
        "content": "AAAAAAAA",
        "is_input": True,
        "style": "2222222",
        "js_path": "2222222",
        "selector": "111111"
    }

    job_title = {
        "content": "AAAAAAAA",
        "style": "2222222",
        "js_path": "2222222",
        "selector": None
    }

    country = {
        "content": "AAAAAAAA",
        "style": "2222222",
        "js_path": "2222222",
        "selector": "111111",
        "optional": True,
        "order": 2
    }

    resume_load_completed = {
        "js_path": "#jobsDocumentCardToggleLabel-ember$$$",
        "optional": False,
        "order": 5
    }

    next_button2 = {
        "style": "artdeco-button__text",
        "text": "Next",
        "js_path": None,
        "is_button": True,
        "selector": None,
        "optional": True,
        "order": 6
    }

    job_about = {
        "style": None,
        "text": None,
        "js_path": None,
        "is_button": False,
        "selector": ["#job-details > div"],
        "optional": True,
        "order": 1
    }

    next_button = {
        "style": "artdeco-button__text",
        "text": "Next",
        "js_path": None,
        "is_button": True,
        "selector": None,
        "order": 3
    }

    resume_load = {
        "is_button": True,
        "text": "upload resume",
        "order": 4,
        "optional": False,
        "selector": ["#ember$$$ > div > div > form > div > div:nth-child(2) > div > div > div > label > span",
                     "#ember$$$ > div > div:nth-child(2) > form > div > div > div > div > div > label > span"]
    }

    experience_years = {
        "style": "2222222",
        "is_input": True,
        "js_path": "#ember317 > div > div:nth-child(2) > form > div > div > div > div > div > label > span",
        "selector": "111111"
    }

    ret_dict = {
        "is_signup_page": False,
        "is_external_page": False,

        "is_normal": True,
        "resume_load": resume_load,
        "job_about": job_about,
        "experience_years": experience_years,
        "next_button": next_button,
        "next_button2": next_button2,
        "f_name": first_name,
        "s_name": second_name,
        "email": email,
        "mobile": mobile,
        "country": country,
        "state": state,
        "address1": address1,
        "job_title": job_title,
        "proposal": proposal,
        "facebook": facebook,
        "zip_code": zip_code,
        "resume_load_completed": resume_load_completed,
        "experience_details": experience_details
    }

    return ret_dict


@app.put("/resume/html")
def recv_resume(input_html: Html):
    # Enviar al LLM
    # llama2_raw_data = llama2_prompt(input_html.content_raw)

    llama2_raw_data = None

    # Parser respuesta del LLM
    llama_data = llama2_parser(llama2_raw_data)

    # Save info into redis
    # result = send_data_redis(444, llama_data)

    return {"response": llama_data}


@app.post("/scrapper/job")
def job_offsets(
    site_flag: int = Body(..., description="Site flag (numeric)"),
    page: int = Body(..., description="Another numeric parameter")
):

    if site_flag == PlatformId.LINKEDIN.value and page == 1:
        # Easy apply
        lnk_dats = LinkedinDats()
        return lnk_dats.get_easy_apply()

@app.post("/llm/test")
def llm_test(input: InputData):
    send_prompt(
        input.linkedin_job_post_title,
        input.linkedin_job_post_description,
        input.skills,
        input.company_name)

    data_to_resume = parser_json()
    data_to_resume["first_name"] = input.first_name
    data_to_resume["last_name"] = input.last_name
    data_to_resume["email"] = input.login_mail
    data_to_resume["login_mail"] = input.login_mail
    return send_to_airesume(data_to_resume)


def parser_project(resp_project):

    if isinstance(resp_project, dict):
        return [resp_project]

    ret_dict = []
    one_dict = {
        "link": "",
        "title": "G00ba beta",
        "overview": "Goomba overview",
        "github": "", "points": ""}

    for single_xp in resp_project:
        one_dict = {"link": "", "title": "", "overview": "", "github": "", "points": ""}

        one_dict["title"] = single_xp.get("title")
        one_dict["overview"] = single_xp.get("overview")
        # var3 = resp_project.get("General Description")
        ret_dict.append(one_dict)

    return ret_dict


def parser_education(education_list):
    ret_dict = []

    for single_education in education_list:
        one_educaction = {
            "title": single_education.get("title"),
            "college": single_education.get("college"),
            "startDate": single_education.get("startDate"),
            "endDate": single_education.get("endDate")}

        ret_dict.append(one_educaction)

    return ret_dict


def parser_work_xp(resp_xp):
    ret_dict = []

    for single_xp in resp_xp:
        one_xp = {
            "certificationLink": "",
            "title": "",
            "startDate": "",
            "endDate": "",
            "companyName": "",
            "location": "",
            "points": []}

        one_xp["companyName"] = single_xp.get("companyName")
        one_xp["title"] = single_xp.get("title")

        one_xp["startDate"] = single_xp.get("startDate")
        one_xp["endDate"] = single_xp.get("endDate")

        points = []
        for responsibility in single_xp.get("points"):
            points.append(responsibility)

        one_xp["points"] = points

        ret_dict.append(one_xp)

    return ret_dict


def parser_achievements(resp_achievements):
    ret_list = []

    for achievement in resp_achievements:
        ret_list.append(achievement)

    return ret_list


def parser_other(resp_other):
    other_list = []
    if isinstance(resp_other[0].get("info"), str):
        return [resp_other[0].get("info")]

    for other in resp_other[0].get("info").keys():
        other_list.append(other)
    return other_list


def parser_json():
    # Summary
    with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_summary.json", "r") as fp:
        raw_resp = json.loads(fp.read())

        if "json_fixed" in raw_resp.keys():
            summary = raw_resp.get("json_fixed")
        else:
            summary = raw_resp.get("response")

        if len(summary) == 0:
            summary_str = ""
        else:
            summary_json = json.loads(summary)

            if "summary" in summary_json.keys():
                summary_str = summary_json.get("summary").get("info")
            else:
                summary_str = summary_json.get("Summary").get("info")

    # Education
    with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_education.json", "r") as fp:
        raw_resp = json.loads(fp.read())

        if "json_fixed" in raw_resp.keys():
            education_dict = raw_resp.get("json_fixed")
        else:
            education_dict = raw_resp.get("response")

        education_list = parser_education(json.loads(education_dict)["education"])

    # Work experience
    with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_employment.json", "r") as fp:
        raw_resp = json.loads(fp.read())

        if "json_fixed" in raw_resp.keys():
            work_dict = raw_resp.get("json_fixed")
        else:
            work_dict = raw_resp.get("response")

        work_list = json.loads(work_dict)
        if isinstance(work_list, list):
            work_xp_list = parser_work_xp(work_list)
        else:
            work_xp_list = parser_work_xp(work_list["work_experience"])

    # Personal project
    with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_personal_projects.json", "r") as fp:
        raw_resp = json.loads(fp.read())

        if "json_fixed" in raw_resp.keys():
            projects_dict = raw_resp.get("json_fixed")
        else:
            projects_dict = raw_resp.get("response")

        if len(projects_dict):
            prj_list = parser_project(json.loads(projects_dict)["personal_project"])
        else:
            prj_list = [{"link":"","title":"lolololo","github":"","points":"","overview":""},{"link":"","title":"","github":"","points":"","overview":""},{"link":"","title":"","github":"","points":"","overview":""},{"link":"","title":"","github":"","points":"","overview":""},{"link":"","title":"","github":"","points":"","overview":""}]

    # Others
    with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_other.json", "r") as fp:
        raw_resp = json.loads(fp.read())

        if "json_fixed" in raw_resp.keys():
            other_dict = raw_resp.get("json_fixed")
        else:
            other_dict = raw_resp.get("response")

        if len(other_dict):
            other_list = parser_other(json.loads(other_dict).get("info_relevant"))
        else:
            other_list = {}

    # Achievements
    with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_achievements.json", "r") as fp:
        raw_resp = json.loads(fp.read())

        if "json_fixed" in raw_resp.keys():
            achievements_dict = raw_resp.get("json_fixed")
        else:
            achievements_dict = raw_resp.get("response")

        achievements_list = parser_achievements(json.loads(achievements_dict)["achievements"])

    return {
        "email": "nada@nada.com",
        "phone": "584129221199",
        "login_mail": "nada@nada.com",
        "xp": work_xp_list,
        "projects": prj_list,
        "title_profile": "turb10",
        "education": education_list,
        "achievements": achievements_list,
        "other": other_list,
        "summary": summary_str
    }


def send_and_save(prompt, save_to):
    ret_code = 0

    ollama_resp = send_to_llm(prompt)
    with open(save_to, "w") as handle:
        ollama_resp["response"] = ollama_resp["response"].replace("\n", "").replace("'", '"')

        try:
            resp_json = json.loads(ollama_resp["response"])
        except:
            print("[!] Trying fix {}".format(save_to.split(".")[0]))
            fix_json_resp = fix_json(ollama_resp["response"])

            if fix_json_resp is not None:
                json_fixed = json.dumps(fix_json_resp.get("json_fix"))
                with open("{}-fix.{}".format(save_to.split(".")[0],save_to.split(".")[1]), "w") as json_fix_fp:
                    json_fix_fp.write(json_fixed)
            else:
                json_fixed = ""
                ret_code = -1

            ollama_resp["json_fixed"] = json_fixed

        handle.write(json.dumps(ollama_resp, indent=2))

        return ret_code


def fix_json(json_str):
    vals_dict = {"json_content": json_str, "token": "cu_15_f67b59c47c9342b1615db0298484ffb85dc974af0f6699b1038ddecf797bb72f"}
    url = "https://api.jsonaut.com/json/v1/repair"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post(url, headers=headers, data=json.dumps(vals_dict))

    if resp.status_code == 200:
        json_obj = json.loads(resp.text)

        if json_obj.get("data").get("json_repaired") == "YES":
            return {"json_fix": json_obj.get("data").get("json_data")}

    return None


def check_and_fix_json(json_prm):
    ret_data = json.loads(json_prm)
    json_obj = ret_data.get("response")
    try:
        resp = json.loads(json_obj)
    except:
        json_fix = fix_json(json_obj)
        ret_data["response"] = json_fix.get("json_fix")

    return ret_data


def send_to_llm(messages):
    config = dotenv_values(".env")
    client = Client(host='{}'.format(config.get("OLLAMA_HOST")))

    response = client.chat(model='llama2:13b', messages=[
        {
            'role': "system",
            'content': messages.get("system")
        },
        {
            'role': 'user',
            'content': messages.get("user")
        },
    ])

    ret_dict = {"system": messages.get("system"), "user": messages.get("user"), "response": response["message"]["content"]}

    return ret_dict


def ss_wrapper(data_prompt, save_to):
    if send_and_save(data_prompt, save_to) != 0:
        for i in range(5):
            print("Trying re-generate ({})".format(str(i)))
            if send_and_save(data_prompt, save_to) == 0:
                i = i
                return i
    return 0


def send_prompt(job_title, linkedin_job_post_description, skills, company_name):
    with open("prompts.json", "r") as fp:
        data = json.loads(fp.read())

        if skills is None:
            # Auto skills
            data["prompts"]["auto_skills"]["system"] = data.get("prompts").get("auto_skills").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name)
            data["prompts"]["auto_skills"]["user"] = data.get("prompts").get("auto_skills").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name)
            ss_wrapper(data["prompts"]["auto_skills"], "dump_auto_skills.json")

            with open("C:\\Users\\os1\\PycharmProjects\\fastapi-002\\dump_auto_skills.json", "r") as fp:
                raw_resp = json.loads(fp.read())

                if "json_fixed" in raw_resp.keys():
                    skills_dict = raw_resp.get("json_fixed")
                else:
                    skills_dict = raw_resp.get("response")

                skills = parser_skills(json.loads(skills_dict)["skills"])

        # Education
        data["prompts"]["education"]["system"] = data.get("prompts").get("education").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        data["prompts"]["education"]["user"] = data.get("prompts").get("education").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        ss_wrapper(data["prompts"]["education"], "dump_education.json")

        # Others
        data["prompts"]["other"]["system"] = data.get("prompts").get("other").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        data["prompts"]["other"]["user"] = data.get("prompts").get("other").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        ss_wrapper(data["prompts"]["other"], "dump_other.json")

        # Achievements
        data["prompts"]["achievements"]["system"] = data.get("prompts").get("achievements").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        data["prompts"]["achievements"]["user"] = data.get("prompts").get("achievements").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        ss_wrapper(data["prompts"]["achievements"], "dump_achievements.json")

        # Summary
        data["prompts"]["summary"]["system"] = data.get("prompts").get("summary").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        data["prompts"]["summary"]["user"] = data.get("prompts").get("summary").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        ss_wrapper(data["prompts"]["summary"], "dump_summary.json")

        # Work experience
        data["prompts"]["employment"]["system"] = data.get("prompts").get("employment").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        data["prompts"]["employment"]["user"] = data.get("prompts").get("employment").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        ss_wrapper(data["prompts"]["employment"], "dump_employment.json")

        # Personal Projects
        data["prompts"]["personal_projects"]["system"] = data.get("prompts").get("personal_projects").get("system").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        data["prompts"]["personal_projects"]["user"] = data.get("prompts").get("personal_projects").get("user").replace("{JOB_TITLE}", job_title).replace("{JOB_DESCRIPTION}", linkedin_job_post_description[:1000]).replace("{COMPANY_NAME}", company_name).replace("{SKILLS}", skills)
        ss_wrapper(data["prompts"]["personal_projects"], "dump_personal_projects.json")


def send_to_airesume(data_from_llm):
    vals_dict = {
        "email": data_from_llm.get("email"),
        "phone": data_from_llm.get("phone"),
        "login_mail": data_from_llm.get("login_mail"),
        "first_name": data_from_llm.get("first_name"),
        "last_name": data_from_llm.get("last_name"),
        "title": data_from_llm.get("title_profile"),
        "address_1": "",
        "address_2": "",
        "summary": data_from_llm.get("summary"),
        "profile_img": "2024/01/335879-scaled4320.jpg",
        "skills": "[]",
        "array1": data_from_llm.get("xp"),
        "array2": data_from_llm.get("projects"),
        "array3": data_from_llm.get("education"),
        "array4": data_from_llm.get("other"),
        "array5": data_from_llm.get("achievements"),
        "theme": "#ed8936",
        "template": ""}

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    json_str = json.dumps(vals_dict)
    result = requests.post("https://resumefalcon.ai/resumeapi/resume/addResume", data=json_str, headers=headers)

    with open("json_sended.json", "w") as fp:
        fp.write(json_str)

    return result.text


def parser_skills(skills):
    ret_str = None
    for skill in skills.get("skillset"):
        if ret_str is not None:
            ret_str = ret_str + ", " + skill
        else:
            ret_str = skill

    return ret_str


def parser_project(resp_project):
    if isinstance(resp_project, dict):
        return [resp_project]

    ret_dict = []

    for single_xp in resp_project:
        one_dict = {"link": "", "title": single_xp.get("title"), "overview": single_xp.get("overview"),
                    "github": single_xp.get("github"), "points": ""}

        ret_dict.append(one_dict)

    return ret_dict


def parser_education(education_list):
    ret_dict = []

    for single_education in education_list:
        one_educaction = {
            "title": single_education.get("title"),
            "college": single_education.get("college"),
            "startDate": single_education.get("startDate"),
            "endDate": single_education.get("endDate")}

        ret_dict.append(one_educaction)

    return ret_dict


def parser_work_xp(resp_xp):
    ret_dict = []

    for single_xp in resp_xp:
        one_xp = {
            "certificationLink": "",
            "title": "",
            "startDate": "",
            "endDate": "",
            "companyName": "",
            "location": "",
            "points": []}

        one_xp["companyName"] = single_xp.get("companyName")
        one_xp["title"] = single_xp.get("title")

        one_xp["startDate"] = single_xp.get("startDate")
        one_xp["endDate"] = single_xp.get("endDate")

        points = []
        for responsibility in single_xp.get("points"):
            points.append(responsibility)

        one_xp["points"] = points

        ret_dict.append(one_xp)

    return ret_dict


def parser_achievements(resp_achievements):
    ret_list = []

    for achievement in resp_achievements:
        ret_list.append(achievement)

    return ret_list


def parser_other(resp_other):
    other_list = []
    if isinstance(resp_other[0].get("info"), str):
        return [resp_other[0].get("info")]

    for other in resp_other[0].get("info").keys():
        other_list.append(other)
    return other_list


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                log_level="debug",
                workers=1)
