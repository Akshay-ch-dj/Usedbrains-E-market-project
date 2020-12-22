# Using Docker and Docker-Compose

---

The essential docker guide with the configuration used in this project, for a more detailed walkthrough and commands with a project [go here](https://github.com/Akshaychdev/Docker-k8s-practice/blob/main/Docs/docker_learn.md)

* Docker is an open source containerization tool.
* Allow the app to run in a lightweight image(lightweight stripped down version of linux os).
* With the help of a docker file, docker installs all the code to run the app.

## Steps to containerize the app

* Create a `Dockerfile` for the project, that contains instructions to build a 'docker image'.
* Put down all the dependencies that needed for the project in Dockerfile.

```dockerfile
FROM python:3.8.6-alpine

LABEL Maintainer="akshaych.dev@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
```

* First one is the `BASE IMAGE` from [docker-hub](https://hub.docker.com/_/python)
* Install pip and copy the requirements.txt file to the build images root.
* Install the dependencies for the libraries, gcc(gnu compiler collection) and zlib.
* `apk` is the package manager for alpine linux(like `apt` in main ubuntu and other distros),
* `add` just adds that package, `--update` registry before adding.
* `--no-cache` not store registry indexes on docker files.
* There are some temporary dependencies, that needed to be present(to unpack the packages) when installing main packages like pillow and psycopg2, ie for pillow( jpeg-dev, libc-dev, zlib-dev, gcc python3-dev..etc), do a search and find the exact dependencies for a package.
* They are installed in `tmp-build-deps` directory and deleted after the install, that makes not efficient build, minimizing the no. of packages.
* After that install the app required files(including django, psycopg) from `requirements.txt`, using pip.
* Make a root directory(here named "app"), for the project, here the source code is stored. Set it as working directory, copy all the local source codes (from the same /app directory here too), to the working directory.
* Make the static and media storing folders in the image root, give them read-write permissions(`chmod -R 755 /vol/web`),
* Create a user for running applications, change the user to created user.

To just build this docker file with docker installed on the system, run `docker build .`

## Using docker-compose

* docker-compose is a tool that allows us to set the runtime features of the docker image and run the project easily from the project location.
* Can say docker builds the docker image, it can be managed using docker-compose.
* The docker compose uses a .yml (yaml) format, file which is a standard format for setting running instructions.
* The sample `docker-compose.yml` for running a django app backed with postgreSQL contains,

  ```yml
  version: "3.7"  # Docker-compose version used(important)

  services:   # List of services need to run
      app:
          build:
              context: .  # build all the directories
          ports:
              - "8000:8000"  # Map the 8000 port, of the docker server for the app
          volumes:
              - ./app:/app  # real time match the directory app(all the changes made to local gets cached to docker server)
          command: >
              sh -c "python manage.py wait_for_db &&   # For the wait for db script
                      python manage.py migrate &&    # do the database migrations
                      python manage.py runserver 0.0.0.0:8000"   # run the server
          # Modifying the app service for db
          environment:
              - DB_HOST=db  # From here django fetches the credentials, from the created environment file
              - DB_NAME=app
              - DB_USER=postgres  # only for test not in production
              - DB_PASS=passwordmain
          depends_on:
              - db

      # Adding database services
      db:
          image: postgres:12-alpine        # Using the postgres alpine image
          volumes:
              - postgres_data:/var/lib/postgresql/data/   # map(named vol) directory to store tables
          ports:
              - "5432:5432"  # default postgres port mapped.
          environment:   # For the use of postgres, login
              - POSTGRES_DB=app
              - POSTGRES_USER=postgres
              - POSTGRES_PASSWORD=passwordmain

  volumes:
      postgres_data:        # Postgress main volume in the container
  ```

* Only change the configuration file in production no source code file change needed for database credentials.
* Use the [docker secrets](https://docs.docker.com/engine/swarm/secrets/) to store sensitive data, if needed.

* To build using docker compose use, `docker-compose build`.
* To run commands in the docker container running, run as shell script as a command "", it is good that the commands stand out in the "".
* To create a new django app,
  `docker-compose run app sh -c "django-admin startproject app ."`
* Note that the `app` is only service in the present docker compose,
* To remove the container after running the command use `--rm` with it, for eg.

  `docker-compose run --rm app sh -c "python manage.py startapp user`

* Use the `docker-compose --help`, to get a list of all possible commands on docker.accordion

IMP:- When running in git bash, or other external terminal in windows, use `winpty` to support certain commands, ie add `winpty` before `docker-compose`.

## Useful commands

* Use $`docker-compose up` to get up and running the container as described in the docker compose and dockerfile in the root.
* Get details of the running container use, `docker inspect`.

### General

* $`docker-machine ip default`  :- To get the docker machine ip (192.168.99.100 usually)
* $`docker-machine --help`  :- To get help with docker-machine management commands.
* $`docker-machine stop`  :- To stop the docker machine from running.

### Manage images and containers

$ -> runs on the bash terminal or linux terminal.

* $`docker ps`  :- See all running containers.
* $`docker ps -a`  :- See all containers(running and existing).
* $`docker container ls`  :- See all containers.(same).
* $`docker images -q`  :- list all images.
* $`docker stop <cont_id/name>`  :- To stop the container.
* $`docker start <cont_id/name>`  :- To start the container.
* $`docker rm <cont_id/name>`  :- Remove container.
* $`docker rmi <image_id>`  :- Remove container.
* One liner to stop and remove all running containers.
  $`docker stop $(docker ps -a -q)`
  $`docker rm -f $(docker ps -a -q)`  // `f` indicated forcibly.
* To remove all docker images.
  $`docker rmi $(docker images -q)`

* remove all containers that aren't running currently.
  $`docker rm $(docker ps -a -q -f"status=exited")` (`-f` -> stream)
* Clean up by removing unnecessary, `docker system prune --all`
* To check the size of all containers use `docker ps -as`

### Docker connect to a running container

* $`docker exec -it <container-name> bash`, it can be used to connect to the db service running and view the tables created in postgres.
* Use `\q` to exit from postgres and `exit` to exit from the terminal.

## Creating docker containers using direct commands.

* Use `docker create` to create a container with `-V` mount a volume, to a specific directory, and --name, name of base image
* To create a running independent db image.accordion

  `docker create -V /var/lib/postgresql/data --name postgres-12.4-db alpine`

* With a env. variables, user and password included, use `docker run`.

  `docker run --name local-db -e POSTGRES_PASSWORD=incorrect -d -p 5432:5432 postgres:alpine`

* Launch a pgadmin,

  `docker run -p 5555:80 --name pgadmin -e PGADMIN_DEFAULT_EMAIL='postgresdb' -e PGADMIN_DEFAULT_PASSWORD='password' dpage/pgadmin4;`

* To build the image `docker build`.

* For logs, `docker logs <c_id>`.