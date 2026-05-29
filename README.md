# Recommender-system 
This is a simple full-stack recommender system built using Python FastAPI for the backend and React for the frontend. Node.js is used for managing the frontend environment, and Docker is used to containerize the application. The project is deployed on Render.

## Tech Stack

* Frontend: React, Node.js
* Backend: Python, FastAPI
* Data/ML: Python (pandas / basic model logic)
* Deployment: Docker, Render

## Project Structure

* frontend/ → React app (UI)
* backend/ → FastAPI server and model
* data.csv → dataset for recommendations
* model.py → recommendation logic
* docker-compose.yml → run full project together

## How it works

User interacts with the React frontend. The frontend sends requests to the FastAPI backend. The backend processes the data using the recommendation logic and returns results to the frontend.

## Run locally

Backend:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:

```bash
npm install
npm start
```

## Docker

To run the full project:

```bash
docker-compose up --build
```

## Deployment

The project is deployed on Render using Docker. Both frontend and backend services are connected and run in the cloud.


---
