
# sk plenet edication docker

## Remove & Get Docker
https://docs.docker.com/engine/installation/

docker rm -f containerId

docker rmi -f dockerImage

apt-get -f install

sudo apt-get remove docker*

curl -s https://get.docker.com/ | sudo sh


## Get Docker-compose
https://github.com/docker/compose/releases

curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose


## Docker-compose up
cd skp_edu_docker/

docker volume create --name=pg_data

docker-compose up


## Pull & Run Docker Image
docker run -itd --env-file=".env" -p 8888:8888 -p 5901:5901 hoyai/tf_edu_docker_skp:v1.2
