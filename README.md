# API Containerization: Movie Recommender System

This repository contains code to containerize a Movie Recommender System API using Docker and push it to GitHub Container Registry (GHCR).

## Repository Design

This repository is designed to facilitate running the Movie Recommender System API in various environments:
1. **GitHub Container Registry (GHCR):** Push the Docker image to GHCR for centralized deployment and pull it back to run locally.
2. **Python Virtual Environment:** Run the system directly in a Python virtual environment for development and testing.
3. **Docker Container (Local):** Containerize the application for local deployment using Docker.


## Getting Started

### Prerequisites

- Python 3.x installed
- Docker installed
- GitHub account and access to GHCR

## 1. GitHub Container Registry (GHCR)

### 1a. Push Docker Image to GHCR

Clone Repo, Build and Tag the Docker image and Push it to GHCR:

```bash
git clone https://github.com/manojbusam/Recommender-Container.git
cd Recommender-Container/
docker build -t movie-recommender-app .
docker tag movie-recommender-app:latest ghcr.io/manojbusam/recommender-container/recommender-system:latest
docker login ghcr.io -u <username> -p <youraccesstoken>
docker push ghcr.io/manojbusam/recommender-container/recommender-system:latest
```

### 1b. Pull and Test from GHCR

Pull the Docker image from GHCR and run it locally:

![Screenshot 2024-07-02 at 9 09 17 AM](https://github.com/manojbusam/Recommender-Container/assets/44409170/1f046e71-490b-430c-a246-dcae90b5933b)

```bash
docker pull ghcr.io/manojbusam/recommender-container/recommender-system:latest
docker run -d -p 5002:5000 ghcr.io/manojbusam/recommender-container/recommender-system:latest
```

Access the API at: [http://localhost:5002/recommend?title=The%20Matrix](http://localhost:5002/recommend?title=The%20Matrix)

<img width="772" alt="Screenshot 2024-07-01 at 7 45 59 PM" src="https://github.com/manojbusam/Recommender-Container/assets/44409170/ea7b9854-4895-4ae6-884a-79669d7b7351">

### 2. Python Virtual Environment  (Local)

2a. **Clone the repository:**

   ```bash
   git clone https://github.com/manojbusam/Recommender-Container.git
   cd Recommender-Container
   ```

2b. **Setup Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2c. **Install Dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

2d. **Run the Recommender System locally:**

   Convert "movies.csv" into a Python file and serve through the recommendations ML model:

   ```bash
   python3 src/recommender.py
   ```

## 3. Docker Container (Local)

### 3a. Build Docker Image

Build the Docker image for the Movie Recommender System API:

```bash
docker build -t movie-recommender-app .
```

### 3b. Run Docker Container

Run the Docker container locally:

```bash
docker run -d -p 5001:5000 movie-recommender-app
```

Access the API at: [http://localhost:5001/recommend?title=The%20Matrix](http://localhost:5001/recommend?title=The%20Matrix)

<img width="581" alt="Screenshot 2024-07-01 at 7 46 06 PM" src="https://github.com/manojbusam/Recommender-Container/assets/44409170/d29f0a21-ec31-49de-b97b-3e66efd78e8a">




