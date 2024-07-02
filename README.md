Here's a proper `README.md` file for your GitHub repository:

```markdown
# Movie Recommender System API Containerization

This repository contains code to containerize a Movie Recommender System API using Docker and push it to GitHub Container Registry (GHCR).

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
```

This `README.md` provides clear instructions for setting up the environment, building the Docker image, pushing it to GitHub Container Registry, and testing it locally. Adjust the URLs and paths as necessary based on your specific setup.
