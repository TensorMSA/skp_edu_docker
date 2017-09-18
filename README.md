
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


## 
docker-compose scale celery=3

##
docker exec -it dockerId bash

move root folder

vi run_celery.sh


##
cd /home/dev/tensormsa

celery -A tensormsa worker -l info
