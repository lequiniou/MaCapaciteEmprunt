# MaCapaciteEmprunt

Personnal project created for learning purposes. The objective is to apply concepts of the following course : https://www.udemy.com/course/docker-mastery/. This project contains two modules:

* mce-backend : a containerized python api to compute and able to log the calls in a local postregreSQL database

* mce-frontend : a streamlit interface on which the users can send its characteristics and call the api

## mce-backend

Back-end (python) for MaCapacitéEmprunt project

### docker build

docker build -t backend-mce . --progress=plain

### docker container run 

docker container run --rm -p 8000:8000 --name mce backend-mce

## mce-frontend