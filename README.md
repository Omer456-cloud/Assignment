# Simple Flask API with Docker - Assignment

This is a simple Flask-based API that returns the current date and time in JSON format. The application is containerized using Docker, making it easy to deploy anywhere.

## **Features**

- Provides an API endpoint that returns the current date and time.
- Dockerized for easy deployment and portability.

## **Technologies Used**

- **Python 3.9**: The programming language used for the backend.
- **Flask**: A lightweight Python web framework.
- **Docker**: Containerization platform for packaging and distributing the application.

## **Installation and Setup**

### **Prerequisites**

Ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (for cloning the repository)

### **Steps to Run Locally**

1. **Clone the repository:**

   If you haven't already cloned the repository, do so by running:

```bash
git clone https://github.com/Omer456-cloud/Assignment.git
cd Assignment

Build the Docker Image
docker build -t flask-api

Run the Docker Container
docker run -p 5000:5000 flask-api

 Access the API
http://localhost:5000/current-time

You should see a response similar to this:
{
  "current_time": "2025-04-10 14:30:00"
}

Stopping the Docker Container
To stop the container, simply go back to the terminal where the Docker container is running and press Ctrl + C. This will stop the Flask server inside the container.

How to Deploy to Cloud (Optional for Extra Credit)
If you need to deploy this application to the cloud (for example, using AWS EC2):

Launch an EC2 instance and install Docker.

SSH into your EC2 instance and clone the repository.

Build and run the Docker container just like in the steps above.

Access the API by visiting the public IP of your EC2 instance (make sure port 5000 is open in your security group).
