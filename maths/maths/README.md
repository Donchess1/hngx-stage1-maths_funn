https://hng.tech/hire/python-developers

#===Project Description===# this is a basic DRF api, built to return the following information in JSON format:

My registered email address (used to register on the HNG12 Slack workspace).
The current datetime as an ISO 8601 formatted timestamp.
The GitHub URL of the project's codebase.
Features Simple GET request to /api/info/ Returns JSON-formatted response Uses Django REST Framework

#===clone and open the git repo==# gitclone https:// cd HNG-api

#===Install Dependencies==# pip install -r requirements.txt

#===Apply Migrations==# python manage.py migrate

#=== Run the Development Server==# python manage.py runserver and access api at http://127.0.0.1:8000/

==>Endpoint URL: GET /api/

==> Request Format: Method: GET Headers: Content-Type: application/json Body: No body required for this request.

==> Response Format: Content-Type: application/json ==> Response Body { "slack_email": "stepabod@yahoo.com", "current_datetime": "2025-01-29T12:34:56.789Z", "github_url": "https://github.com/Donchess1/Myproject.git" } ==> Request Example curl -X GET http://127.0.0.1:8000/api/