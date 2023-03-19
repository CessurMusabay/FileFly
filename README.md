# FileFly

This is a Django REST API server that allows you to upload and download files through HTTP requests. It uses Django's built-in authentication system to secure the endpoints.


## Features

* Upload and download files through HTTP requests.
* Easy to use and configure.

## Installation
1. Clone the repository
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the server: `python manage.py runserver`

## Endpoints

*`POST /upload/`: Upload a file.
*`POST  /download/:id`: Download a file by ID. Requires authentication.
*`GET  /transfer/:id`: Get file information.