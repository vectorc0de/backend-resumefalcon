class LinkedInScraper:
    def get_easy_apply_selectors(self):
        return {
            "job": {
                "description": {
                    "style": None,
                    "js_path": None,
                    "selector": ["#job-details > div"]
                },
                "skills": {},
                "job_title": {}
            },
            "apply_job": {
                "email": {
                    "content": [],
                    "is_input": True,
                    "style": None,
                    "js_path": [],
                    "selector": []
                },
                "next_button": {
                    "style": ["artdeco-button__text"],
                    "text": "Next",
                    "js_path": None,
                    "is_button": True,
                    "selector": None,
                    "order": 3,
                    "optional": True
                },
                "country": {
                    "content": [],
                    "style": [],
                    "js_path": [],
                    "selector": [],
                    "optional": True,
                    "order": 2
                },
                "next_button2": {
                    "style": ["artdeco-button__text"],
                    "text": "Next",
                    "js_path": None,
                    "is_button": True,
                    "selector": None,
                    "order": 6
                },
                "mobile": {
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
                },
                "resume_load_completed": {
                    "js_path": ["#jobsDocumentCardToggleLabel-ember$$$"],
                    "selector": ["#ember358"],
                    "style": ["artdeco-button artdeco-button--2 artdeco-button--primary ember-view"],
                    "is_pattern": True,
                    "order": 5,
                    "text": "submit",
                    "optional": False
                },
                "resume_load": {
                    "is_button": True,
                    "text": "upload resume",
                    "order": 4,
                    "optional": True,
                    "selector": ["#ember$$$ > div > div > form > div > div:nth-child(2) > div > div > div > label > span",
                                 "#ember$$$ > div > div:nth-child(2) > form > div > div > div > div > div > label > span"]
                }
            }
        }
