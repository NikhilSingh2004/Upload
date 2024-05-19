# Upload File Project

Welcome to Upload file project, a simple project demonstrating the use of FastAPI, the API is containerized using Dokcer.

## Clone the project

To get started with the project, you can clone the repository to your local machine using the following command:

`git clone https://github.com/NikhilSingh2004/Upload.git`

After cloning the repository, you can navigate to the project directory.

## Directory Structure 

Keep in mind the following Directory Structure

techscholar-backend-123456/
├── uploaded_files/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── tests/
│       ├── __init__.py
│       ├── test_main.py
├── Dockerfile
├── .dockerignore
├── docker-compose.yaml
├── .gitignore
├── requirements.txt
└── README.md

## Install Project

After cloning the repository you will have to build an local Docker Container.

Navigate to the Directory where you can find the `Dokcerfile`, after that run the following command

`docker compose up --build`

The above command will create an local Docker container containing the project, it will aslo run the 'Uvicorn' Server

Now open any Broswer & in the search bar type `http://127.0.0.1:8000`

If every thing goes will then the output will be :

{
  "detail": "Not Found"
}

This is because there is no endpoint at '/'

## API Documentation

The API documentation provides details about the endpoints, request and response formats. You can find the API documentation hosted on postman.

Here's how you can access the API documentation:

1. Navigate to `https://documenter.getpostman.com/view/34873005/2sA3QmCuTe`

## Run Test Cases

The project includes unit tests to ensure the correctness of the implemented functionalities. To run the test cases, follow these steps:

1. Navigate to the project directory.
2. Activate your virtual environment (if you're using one).
3. Run the following command:

`pytest app/tests/test_main.py `

This command will execute all the unit test cases and provide the test results.
