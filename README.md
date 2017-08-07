
# sk plenet edication docker

## Get Docker
https://docs.docker.com/engine/installation/

## Get Docker-compose
https://github.com/docker/compose/releases

curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose


## Pull & Run Docker Image
docker run -itd --env-file=".env" -p 8888:8888 -p 5901:5901 hoyai/tf_edu_docker_skp:v1.0

## Docker-compose up
docker-compose up
