## Getting started with Docker and Redis

You need to setup redis in Docker in order to have a better system of dealing with it.
A redistributable software component


sudo pacman -S docker
docker pull redis:alpine


**docker set-up**
sudo systemctl status docker
```commandline
sudo systemctl enable docker
sudo systemctl start docker
```

Don't forget to config abr arvar
https://www.arvancloud.ir/fa/dev/docker

```commandline
sudo docker pull redis:alpine
sudo docker run --rm -d --name "maktab_redis" -p "5555:6379" redis:alpine
sudo docker exec -it maktab_redis redis-cli
```


** when we are using docker we don't need them **
```commandline
sudo systemctl enable radis
sudo systemctl disable radis
```

redis insight

Python ORM for REdis:
https://pypi.org/project/hiredis/
https://pypi.org/project/redis/
