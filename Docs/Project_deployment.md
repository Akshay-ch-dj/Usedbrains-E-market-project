# Project Deployment to Heroku <!-- omit in toc -->

<!-- omit in toc -->
## Table of Contents

- [Reference resources From previous projects](#reference-resources-from-previous-projects)
- [Modifying docker file for deployment](#modifying-docker-file-for-deployment)
- [Django setup for Postgres with Docker (for Heroku)](#django-setup-for-postgres-with-docker-for-heroku)
- [Setup heroku app](#setup-heroku-app)
- [Deployment to heroku using Container Registry](#deployment-to-heroku-using-container-registry)
- [Postgress Database creation on heroku](#postgress-database-creation-on-heroku)
- [External references docs](#external-references-docs)

## Reference resources From previous projects

* For a detailed information on setting docker file for deployment [view this sample project](https://github.com/Akshaychdev/Heroku-Docker-Django-Tester/blob/deployment/Docs/django_deployment.md).
* For detailed information on docker and containerization view this [documentation](https://github.com/Akshaychdev/Docker-k8s-practice/blob/main/Docs/docker_learn.md).
* The initial development docker config for [this project and basic commands](docker_essentials.md)

## Modifying docker file for deployment

 ```Dockerfile
  FROM python:3.8.6-alpine

  LABEL Maintainer="akshaych.dev@gmail.com"

  ENV PYTHONUNBUFFERED 1
  ENV PYTHONDONTWRITEBYTECODE 1


  COPY ./requirements.txt /requirements.txt

  # The initial dev. config for reference
  # RUN apk add --update --no-cache postgresql-client jpeg-dev
  # RUN apk add --update --no-cache --virtual .tmp-build-deps \
  #   gcc libc-dev  postgresql-dev musl-dev zlib zlib-dev
  # RUN pip install -r /requirements.txt
  # RUN apk del .tmp-build-deps
  # RUN mkdir /app

  RUN set -ex \
    && mkdir /app \
    && pip install --upgrade pip \
    && apk add --update --no-cache postgresql-libs jpeg-dev \
    && apk add --update --no-cache --virtual .tmp-build-deps \
    gcc musl-dev postgresql-dev zlib zlib-dev linux-headers \
    && pip install --no-cache-dir -r /requirements.txt \
    && apk --purge del .tmp-build-deps

  WORKDIR /app
  COPY ./app /app

  RUN mkdir -p /vol/web/media \ # not used now
      && mkdir -p /vol/web/static \  # not used now
      && adduser -D user \  # Add a user for server
      && chown -R user:user /vol/ \
      && chown -R user:user /app \
      && chmod -R 755 /vol/web

  USER user

  CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
 ```

* The size needs to minimized for deployment, chain the commands to increase building speed and remove the creation of unwanted containers.
* The `set -ex` command, while `set -x` enables a mode of the shell where all executed commands are printed to the terminal, printing every command as it is executed may help you to visualize the control flow of the script if it is not functioning as expected.
* The `set -e`, aborts the execution of a command (e.g. a shell script) and returns the exit status code of the command that failed (i.e. the inner script, not the outer script).
* `--purge` removes everything related to a package including the configuration files.
* Set user as the owner of the "app" folder(temporary solution until separating static)
* The `$PORT` variable. Essentially, any web server that runs on the Container Runtime must listen for HTTP traffic at the `$PORT` environment variable, which is set by Heroku at runtime.

* Install the additional packages for heroku and update the `requirements.txt`, added packages, gunicorn,whitenoise, dj-database-url, django-storages
* The `requirements.txt` file now,

  ```txt
  Django>=3.0.7,<3.1.0

  psycopg2>=2.8.5,<2.9.0
  Pillow>=7.2.0,<7.3.0
  dj-database-url>=0.5.0,<0.6.0
  django-storages>=1.11.1,<1.12.0
  gunicorn>=20.0.4,<20.1.0
  whitenoise>=5.2.0,<5.3.0
  python-dotenv>=0.15.0,<0.2.0
  ```

* Using `pip show <module_name>` to get information about a pip installed module.
* Set environment variables local using `dotenv`.
* Modify other settings to support, whitenoise, dj-database-url, find the sample [here.](https://github.com/Akshaychdev/Heroku-Docker-Django-Tester/blob/deployment/core/settings/settings.py)

* Do a local test, build the image and run the container, making sure to pass in the appropriate environment variables:

  ```console
  docker build -t web:latest .
  docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
  ```

* That sets the `$PORT` variable explicitly and which is bounded to host port `8007`, now (`127.0.0.1:8007`) it can be run locally.
* Shift to `sqlite` for local testing  run give permissions for the sqlite read and write. Quick look [here](https://www.pluralsight.com/blog/it-ops/linux-file-permissions) for basic info on linux permissions, eg `755`(commonly used by web servers.) The owner has all the permissions to read, write and execute. Everyone else can read and execute but cannot make changes to the file.
* Modified docker file for local testing before deployment,

  ```Dockerfile
  # ... as previous

  RUN mkdir -p /vol/web/media \ # not used now
      && mkdir -p /vol/web/static \  # not used now
      && adduser -D user \  # Add a user for server
      && chown -R user:user /vol/ \
      && chown -R user:user /app \
      && chmod -R 755 /vol/web

  USER user

  RUN python manage.py migrate

  CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
  ```

## Django setup for Postgres with Docker (for Heroku)

* For heroku add dependency [`dj_database_url`](https://pypi.org/project/dj-database-url/) to the requirements(above), that generates a proper database configuration dictionary for the Django settings based on a `DATABASE_URL` environment variable, als import to the top as well, `import dj_database_url`.
* Changes to the settings to update the database configuration if the `DATABASE_URL` is present:
* Also use sqlite3 as a backend, so, if the `DATABASE_URL` is not present, SQLite will still be used.(optional)

  ```py
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }

  DATABASE_URL = os.environ.get('DATABASE_URL')
  db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
  DATABASES['default'].update(db_from_env)
  ```

## Setup heroku app

* login to heroku using CLI (`heroku login`), create a new app (`heroku create ub-app-v1`),
* Add environment variables using dashboard settings or using CLI,

  ```sh
  heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a ub-app-v1
  ```

* Update the allowed hosts, add the `ub-app-v1.herokuapp.com`

## Deployment to heroku using Container Registry

* Deploying pre-built Docker images to Heroku.
* Login to the [Heroku container registry](https://devcenter.heroku.com/articles/container-registry-and-runtime), `heroku container:login`
* Re-build the Docker image and tag it with the format: `registry.heroku.com/<app>/<process-type>`. Here `<app>` is `ub-app-v1` and `<process-type>` with web since this will be for a [web process](https://devcenter.heroku.com/articles/procfile#the-web-process-type), ie\

  `docker build -t registry.heroku.com/ub-app-v1/web .`

* Push the image to the registry: `docker push registry.heroku.com/ub-app-v1/web`

* It can be combined to a single command with:- `heroku container:push web -a=ub-app-v1`

* Release the image and open it,

  ```shell
  heroku container:release -a ub-app-v1 web
  heroku open -a ub-app-v1
  ```

* To view the staticfiles served, `heroku run ls /app/staticfiles -a ub-app-v1`

## Postgress Database creation on heroku

* Heroku [postgres documentation](https://devcenter.heroku.com/articles/heroku-postgresql).
* Create the database:-

  ```console
  heroku addons:create heroku-postgresql:hobby-dev -a ub-app-v1
  ```

  "hobby-dev" is the free plan for the postgres addon and this command automatically sets the `DATABASE_URL` environment variable for the container.

* Use the `heroku addons` command to view addons and `heroku config` to view configurations set up(env variables DB_URLS ..etc)
* For logging use `heroku logs -t` and `heroku logs -p postgres -t`, also `pg:diagnose` is very helpful,\
  `heroku pg:diagnose -a ub-app-v1`

* Once the database is up, run the migrations, \

  ```shell
  heroku run python manage.py makemigrations -a ub-app-v1
  heroku run python manage.py migrate -a ub-app-v1
  ```

* For general info on size and tables, `heroku pg:info`, to connect to `psql` use `heroku pg:psql`

  ```sh
  heroku pg:psql -a ub-app-v1

  # \dt

  <tables>

  # \q   (to quit from psql)
  ```

## External references docs

* [Django-heroku app deployment](https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43)
* [Django-Docker-Heroku-Postgress app deployment](https://testdriven.io/blog/deploying-django-to-heroku-with-docker/)
* [Dockerizing django with postgres, gunicorn and nginix.](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
* Building python apps with [docker base image comparison.](https://pythonspeed.com/articles/alpine-docker-python/)
