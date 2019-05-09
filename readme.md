# GRCP Client Server Model

This application demonstrates the basic client server model writing microservices using GRCP

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
* Python3.6 (or) Docker-compose
```

### Installing

A step by step series of examples that tell you how to get the project up and running

#### Using Python

* Create a virtual environment using `virtualenv name`

* Navigate to the `client` dir and then do `pip install -r requirements.txt` . This should get all the client requirements installed

* Next Navigate to `server` dir and then do `pip install -r requirements.txt` . This should get all the server requirements installed

* Start the client

Before starting the client make sure you export the cloudinary url<br>

```
export CLOUDINARY_URL=cloudinary://663314969728525:yENrtmlHycsoRVV9PC_1jl5sDZw@shara
cd client
python app.py
(or)
python wsgi.py
(or)
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
* Start the server
```
cd server
python main.py
```

#### Using Docker
* Make sure `docker-compose` is installed

* Just from the root directory run 
```
docker-compose -f local.yml up  # for starting the entire stack
docker-compose -f local.yml down # for bringing down the entire stack
docker-compose -f local.yml build # for building the stack
```
Navigate to localhost:3000 and you can find the flask service running