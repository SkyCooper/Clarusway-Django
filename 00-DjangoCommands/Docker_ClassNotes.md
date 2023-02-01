@victor hoca docker notları,

# Server Systems

- Physical Servers (BareMetal Servers):

  - Bilgisayar -> Yüksek donanım, özel işlemciler, özel işletim sistemleri.
  - Kurulum: zor
  - VeriTaşıma: zor
  - Maliyet: yüksek
  - Dedicated Servers

- Virtual Servers (VMs: Virtual Machines):

  - Bir fiziksel makina içinde çok sanal makina.
  - Kurulum: orta (iso image)
  - VeriTaşıma: orta
  - Maliyet: orta
  - Bir makiaden diğer makinaya geçiş zorluğu.
  - Hypervisor yazılımları -> vmware.com
  - VPS (Virtual Private Server), VDS (Virtual Dedicated Server)

- Containers:
  - Bir fiziksel/sanal makina içinde çok konteyner.
  - Kurulum: kolay (docker image)
  - VeriTaşıma: kolay
  - Maliyet: düşük
  - Tüm konteynerları aynı ortamdan yönetebilme.
  - Microservice mimarisi.
  - Container yazılımları -> docker.com

## Temel Bilgiler

- IP ve Port mantığı
- Default portlar 80 443 -> https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
- http -> 80 \* http://clarusway.com == http://clarusway.com:80
- https -> 443 \* https://clarusway.com == https://clarusway.com:443 (need SSL)

---

# Docker

## Yüklemeler:

- Docker Desktop -> https://www.docker.com/products/docker-desktop/

  - Windows ve Macos için setup dosyası mevcut.
  - Linux sistemlere CLI üzerinden kurulum yapılabilir. -> https://docs.docker.com/desktop/install/linux-install/

- Docker Hub -> https://hub.docker.com

- VSCode Docker Extension -> https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker

## .dockerignore

create .dockerignore file for per project:

```dockerignore

*.pyc
*.pyo
*.mo
*.db
*.css.map
*.egg-info
*.sql.gz
.cache
.project
.idea
.pydevproject
.idea/workspace.xml
.DS_Store
.git/
.sass-cache
.vagrant/
__pycache__
dist
docs
env/
logs
src/{{ project_name }}/settings/local.py
src/node_modules
web/media
web/static/CACHE
stats
Dockerfile
Footer
node_modules/
npm-debug.log

```

## DOCKERFILE

- https://docs.docker.com/engine/reference/builder/
- create file, named "dockerfile" (no extension)

backend/dockerfile:

```dockerfile

# --- Build Start ----

# Python
# Last Version
# FROM python
# Light Versiyon
FROM python:3.11.1-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set main folder in container:
# WORKDIR /
WORKDIR /backend

# copy all from local-files (.) to docker (/backend):
COPY . /backend

# Run shell-command in docker before build:
RUN pip install -r requirements.txt --no-cache-dir

# --- Build End ----

# --- Run Start ---

# Run shell-script:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# App Port (optional)
EXPOSE 8000

# --- Run Start ---

# $ cd /backend
# Create Image:
# $ docker build -t backend .
# Create and Start Container:
# -d -> Daemon Mode
# $ docker run -d -p 8000:8000 --name backend backend
# Browser: http://localhost:8000


```

frontend/dockerfile:

```dockerfile

# NodeJS
FROM node:19-slim

# Set main folder in docker:
WORKDIR /frontend
# Copy file local to docker:
COPY package.json /frontend/package.json

# Run shell-command in docker before build:
RUN npm install

# copy all local-files (.) to docker (/frontend):
COPY . /frontend

# Run shell-script:
CMD ["npm", "start"]
# App Port (optional)
EXPOSE 3000

# $ cd /frontend
# $ docker build -t frontend .
# $ docker run -d -p 3000:3000 --name frontend frontend
# Browser: http://localhost:3000

```

## Komutlar:

- https://docs.docker.com/get-started/docker_cheatsheet.pdf

```sh

    $ docker --version # Check version
    $ docker version # Check version with details
    $ docker info # Check info
    $ docker help # Run help and see all commands
    $ docker <command> --help # Run help for any command.
    $ docker system prune -a # Stop and delete passive containers/images/caches.

    # ! It can write image_id instead of image_name.
    # ! It can write container_id instead of container_name.

    # Build Files to Image:
    $ docker build -t <image_name> <folder_name> # Create images from dockerfile.
    $ docker build -t <user_name>/<image_name> .

    # Run Image to Container: (allways, image_name must be on the end):
    $ docker run -d -p <ext_port_number>:<int_port_number> <image_name> # run with external/internal port
    $ docker run -it <image_name><terminal> # run docker with interctive mode, default terminal bash
    $ docker run -d --name <container_name> <image_name> # run and set container name
    $ docker run -d -p <ext_port_number>:<int_port_number> --name <container_name> <image_name>

    # IMAGES:
    $ docker images # List local images.
    $ docker image ls # List local images.
    $ docker rmi <image_name> # Delete image.

    # CONTAINERS:
    $ docker container ls # List local container.
    $ docker ps # List active containers.
    $ docker ps -a # docker ps --all # List all containers.
    $ docker start|stop <container_name> # Start/Stop container.
    $ docker rm <container_name> # Delete stopped container.
    $ docker container prune # delete all stopped container

    # DOCKERHUB:
    $ docker login # Login auto (get user-info from docker-desktop)
    $ docker login -u <user_name> # Login manual
    $ docker tag <image_name> <user_name>/<image_name>[:tag] # Connect repo and set tag
    $ docker push <user_name>/<image_name>[:tag] # PUSH
    $ docker pull <user_name>/<image_name>[:tag] # PULL
    $ docker search <image_name> # Search in DockerHub

```

---

# Docker Compose

- https://docs.docker.com/compose/compose-file/

/docker-compose.yml:

```yml
# version: "3.9" # optional

services:
  frontend:
    container_name: frontend
    image: docker-compose-fronted
    build: ./frontend
    ports:
      - 3000:3000
      - 80:3000
    restart: on-failure
    depends_on:
      - backend # first run backend.

  backend:
    # container_name: backend # optional (default:key)
    image: docker-compose-backend # build, if no image
    build: ./backend # Which folder (project folder) (must be dockerfile in the folder)
    ports: # external:internal ports
      - 8000:8000
    restart: on-failure # when restart
    volumes: # external:internal volumes
      - ./backend/db.sqlite3:/backend/db.sqlite3
# $ docker compose up # compose çalıştır.
# $ docker compose up -d --build # compose daemon aç ve tekrar build et.
# $ docker compose down # compose kapat.
```

---

### Bonus: SuperMario:

```sh

    $ docker run -d -p 8600:8080 bharathshetty4/supermario
    # open http://localhost:8600

  docker-compose exec backend python manage.py migrate --noinput

```
