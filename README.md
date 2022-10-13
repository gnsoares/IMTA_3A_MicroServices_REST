# UE-AD-A1-REST (TP GREEN)

The project is composed of 4 services each one with its own folder. The services are:
* `movie`
* `showtime`
* `booking`
* `user`

Each service runs using Python 3.10

Inside each folder you will find:
* Main server file (`*.py`)
* Dockerfile to build service image
* Python library requirements (`requirements.txt`)
* OpenAPI specification (`*.yaml`)
* `databases` folder with the `.json` file that holds the service data
* `templates` folder with the `.html` file of the service index

Beyond that, a `ui` folder holds files that allow for better visualization of the OpenAPI specifications and the `docker-compose.yml` is used to run the services using docker.

### Running locally

```
SERVICE = "movie" | "showtime" | "booking" | "user"
cd ${SERVICE}
python3.10 ${SERVICE}.py [-H HOST] -p PORT
```

### Running with Docker

```
docker-compose up [--build] ${SERVICE}
```

