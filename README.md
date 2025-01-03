# MaCapaciteEmprunt

Personal project created for learning purposes. The objective is to apply concepts from the following course: [Docker Mastery](https://www.udemy.com/course/docker-mastery/). The resulting application is a Borrowing Power Calculator. This project contains two modules:

- **mce-backend**: A containerized Python API to compute borrowing power and log API calls in a local PostgreSQL database (when provided).
- **mce-frontend**: A Streamlit interface where users can input their characteristics and call the API.

## Install Requirements

```bash
python3.10 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## create a docker network for the app

```bash
docker network create mce-network
```

## launch mce-backend

Back-end (python) for MaCapacitéEmprunt project

1. docker build

Inside **mce-backend/** :
```bash
docker build -t mce-backend . --progress=plain
```

2. docker container run 

```bash
docker container run --rm -p 8000:8000 --name mce-backend --network mce-network mce-backend
```

## launch mce-frontend

Front-end (python) for MaCapacitéEmprunt project

1. docker build

Inside **mce-frontend/** :

```bash
docker build -t mce-frontend . --progress=plain
```

2. docker container run 

```bash
docker container run --rm -p 8080:8080 --name mce-frontend --network mce-network mce-frontend
```

## launch both frontend & backend at the same time

From the root :

```bash
docker compose up
```

To shut it down: 

```bash
docker compose down
```
