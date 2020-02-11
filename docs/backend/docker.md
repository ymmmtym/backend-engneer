# Docker
## Install for centos
**Install docker**
```
sudo yum -y update
sudo yum -y install git docker docker-compose
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo systemctl restart docker
```

### Init setting
**delete sudo authority for docker cmd**
```
sudo groupadd docker
sudo gpasswd -a ${USER} docker
```

## Commands
**copy**
```
docker cp -r ${container_id}:${input} ${output}
```

**run with mounting volumes**
```
docker run -v /home/hoge/shared:/shared -d -it ubuntu /bin/bash
```

**show `<none>` images**

```
docker images -f "dangling=true"
```

**build with tag**
```
docker build -t ${USER}/${tagname} .
```

**delete**
```
docker container prune
docker volume prune
docker image prune
docker network prune
docker system prune --volumes
```

**tag**
```
docker pull ${USER}/${image}
docker tag ${USER}/${image} ${USER}/${image}:${tag}
docker push ${USER}/${image}:${tag}
```

## Terraform

**Use docker image**
```
docker run -it -v $PWD:/app -w /app hashicorp/terraform apply
```

## Dockerhub
1. puth image to dockerhub
2. connect to github
3. setting automated build


## Dockerfile
default directory is /
If workdir not exist, created automatelly.