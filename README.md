# (WIP) Premium Support Dashboard - Backend

Backend to provide the data that will be displayed in the Premium Support dashboard.

---

### Running the Project locally

- Clone the repository
- Run the script `./start`
  (_This creates the virtual env and starts the server_)
- The server will be at: http://localhost:8000

The provided script can also start the application server and the Locust tool for performance testing. You can start them both by running: `./start --locust`

To check the API documentation of the application, open the URL: http://localhost:8000/docs

---

### Running the locust load testing tool (Without using the script)

- Clone the repository
- Run the main fastapi application: `uvicorn main:app --reload`
- Run the Locust tool: `locust -f performance_tests/locustfile.py --host=http://127.0.0.1:8000`
- Open a browser to access the dashboard: http://localhost:8089/
