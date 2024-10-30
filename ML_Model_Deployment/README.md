# ML Model Deployment using FastAPI and Docker

This repository contains all necessary files and instructions for deploying a machine learning model using FastAPI and Docker.

## Setup and Deployment Instructions

### Step 1: Generate Joblib File
Run `importjoblib.py` to save the trained model as a joblib file.

```bash
python importjoblib.py
```

This will create a joblib file, which is essential for deploying the model within the container.

### Step 2: Build Docker Image
Build a Docker image using the following command:

```bash
docker build -t <image_name> .
```
Replace <image_name> with a name of your choice for the Docker image.

### Step 3: Run Docker Container
To run the container, use:

```bash
docker run --name <container_name> -p 8000:8000 <image_name>
```
Replace <container_name> with a name for the container, and ensure the image name matches the one used in the build command.

### Step 4: Access the Model Interface
You can interact with the model deployment in two ways:

- **Web Interface**: Open a browser and go to [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs) to access API documentation.
- **Client Script**: Run the `client.py` script to test the model's output programmatically.


  
### Additional Notes

- Ensure Docker is installed on your machine and that you have internet access to pull any required base images.
- The created Docker container can be deployed on AWS using services like Amazon Elastic Container Service (ECS) or Amazon Elastic Kubernetes Service (EKS). Follow these general steps:
  1. **Push the Docker Image to Amazon ECR**:
    - First, create an Amazon ECR repository to store your Docker image.
    - Authenticate Docker to your Amazon ECR registry.
    - Tag your Docker image:
     ```bash
     docker tag <image_name>:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:latest
     ```
    - Push the Docker image:
     ```bash
     docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:latest
     ```

  2. **Deploy on Amazon ECS**:
    - Create a new ECS cluster.
    - Define a task definition that includes the image URI of your Docker container.
    - Launch a new service within your ECS cluster using the task definition.

  3. **Access the Deployed Service**:
    - After deployment, you can access your service using the public IP or domain name provided by AWS.


