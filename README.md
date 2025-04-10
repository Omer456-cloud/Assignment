# Simple Flask API with Docker - Assignment

This is a Python Flask application that returns the current date and time when accessed at the `/current-time` endpoint. The project is Dockerized for easy deployment.


## Requirements

To run this project, you need to have the following installed:

- **Docker**: Ensure Docker is installed on your system.
- **Git**: To clone the repository.

## Steps to Run the Project

### 1. Clone the GitHub Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name

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
