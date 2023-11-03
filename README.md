# FastAPI-Random-Postman

This small program is a FastAPI application written in Python. It has two endpoints: '/' and '/random/{limit}'.

The root endpoint ('/') responds with a simple message when you make a GET request to it.

The '/random/{limit}' endpoint generates a random number between 0 and the specified 'limit' when you make a GET request to it. The 'limit' is a parameter you provide in the URL, and the endpoint returns a JSON response with the generated number and the provided limit.

To run this program, you can use a tool like 'uvicorn' to start the FastAPI server, like this:

Once the server is running, you can test the '/random/{limit}' endpoint with a tool like Postman. Send a GET request to 'http://127.0.0.1:8000/random/99999999' to get a random number between 0 and 99999999. The response will be in JSON format and will include the generated number and the specified limit.

This program demonstrates the use of FastAPI for building web APIs and how to make HTTP requests to its endpoints using tools like Postman for testing."
