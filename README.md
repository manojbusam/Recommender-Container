# Movie Recommender System API Containerization

This repository contains code to containerize a Movie Recommender System API using Docker and push it to GitHub Container Registry (GHCR).

## Repository Design

This repository is designed to facilitate running the Movie Recommender System API in various environments:
- **Python Virtual Environment:** Run the system directly in a Python virtual environment for development and testing.
- **Docker Container (Local):** Containerize the application for local deployment using Docker.
- **GitHub Container Registry (GHCR):** Push the Docker image to GHCR for centralized deployment and pull it back to run locally.

## Getting Started

### Prerequisites

- Python 3.x installed
- Docker installed
- GitHub account and access to GHCR

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/manojbusam/Recommender-Container.git
   cd Recommender-Container
   ```

2. **Setup Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Run the Recommender System locally:**

   Convert "movies.csv" into a Python file and serve through the recommendations ML model:

   ```bash
   python3 src/recommender.py
   ```

## Docker Containerization

### Build Docker Image

Build the Docker image for the Movie Recommender System API:

```bash
docker build -t movie-recommender-app .
```

### Run Docker Container

Run the Docker container locally:

```bash
docker run -d -p 5001:5000 movie-recommender-app
```

Access the API at: [http://localhost:5001/recommend?title=The%20Matrix](http://localhost:5001/recommend?title=The%20Matrix)

<img width="581" alt="Screenshot 2024-07-01 at 7 46 06 PM" src="https://github.com/manojbusam/Recommender-Container/assets/44409170/d29f0a21-ec31-49de-b97b-3e66efd78e8a">


## GitHub Container Registry (GHCR)

### Push Docker Image to GHCR

Tag the Docker image and push it to GHCR:

```bash
docker tag movie-recommender-app:latest ghcr.io/manojbusam/recommender-container/recommender-system:latest
docker login ghcr.io -u manojbusam -p <youraccesstoken>
docker push ghcr.io/manojbusam/recommender-container/recommender-system:latest
```

### Pull and Test from GHCR

Pull the Docker image from GHCR and run it locally:

```bash
docker pull ghcr.io/manojbusam/recommender-container/recommender-system:latest
docker run -d -p 5002:5000 ghcr.io/manojbusam/recommender-container/recommender-system:latest
```

Access the API at: [http://localhost:5002/recommend?title=The%20Matrix](http://localhost:5002/recommend?title=The%20Matrix)

<img width="772" alt="Screenshot 2024-07-01 at 7 45 59 PM" src="https://github.com/manojbusam/Recommender-Container/assets/44409170/ea7b9854-4895-4ae6-884a-79669d7b7351">

