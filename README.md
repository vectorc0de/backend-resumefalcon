# ResumeFalcon Backend

This is the backend service for ResumeFalcon, an application designed to automate and assist with the job application process. It provides an API to handle job data, process information, and interact with various job platforms.

## Features

*   RESTful API for managing job application data.
*   Scalable and modular architecture using Object-Oriented Programming.
*   Automated testing pipeline with GitHub Actions.
*   (Planned) Integration with Large Language Models (LLMs) for parsing job descriptions.
*   (Planned) Web scraping capabilities to interact with job platforms.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.10 or newer
*   pip

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/vectorc0de/backend-resumefalcon.git
    cd backend-resumefalcon
    ```

2.  Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

To start the development server, run the following command from the project root:

```sh
python main.py
```

The application will be running and available at `http://127.0.0.1:8000`.

## Running Tests

To run the automated tests, execute the following command from the project root:

```sh
pytest
```

## API Endpoints

### Update Job

*   **URL:** `/jobs`
*   **Method:** `PUT`
*   **Description:** Updates or creates a job entry.
*   **Request Body:**

    ```json
    {
      "linkedin_job_post_title": "string",
      "linkedin_job_post_description": "string",
      "first_name": "string",
      "last_name": "string",
      "login_mail": "string",
      "company_name": "string",
      "skills": "string"
    }
    ```

*   **Success Response:**

    ```json
    {
      "message": "string"
    }
    ```

## Project Structure

```
backend-resumefalcon/
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI workflow
├── src/
│   ├── api/            # FastAPI application, routers, and endpoints
│   │   ├── endpoints/
│   │   └── server.py
│   ├── core/           # Core components like database clients
│   │   └── redis_client.py
│   ├── models/         # Pydantic data models
│   │   └── job_data.py
│   └── services/       # Business logic and external service integrations
│       └── linkedin_scraper.py
├── tests/              # Unit and integration tests
│   └── test_api.py
├── main.py             # Main application entry point
├── requirements.txt    # Project dependencies
└── README.md           # This file
```
