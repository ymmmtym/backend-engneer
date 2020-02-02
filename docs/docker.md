# Docker
## install for centos
```
sudo yum -y update
sudo yum -y install git docker docker-compose
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo systemctl restart docker
```

### init setting
delete sudo authority for docker cmd
```
sudo groupadd docker
sudo gpasswd -a $USER docker

exit
```

## Commands
copy
```
docker cp ${container_id}:${dir} ${output_dir}
```

prune unused containers and images
```
docker system prune
```

run with mounting volumes

```
docker run -v /home/hoge/shared:/shared -d -i -t ubuntu /bin/bash
```

show `<none>` images

```
docker images -f "dangling=true"
```

build with tag
```
docker build -t ${USER}/${tagname} .
```

delete

```
docker container prune
docker volume prune
docker image prune
docker network prune
docker system prune --volumes
```

tag

```
docker pull ${USER}/image
docker tag ${USER}/image ${USER}/image:1.0
docker push ${USER}/image:1.0
```

### terraform

```
docker run -it -v $PWD:/app -w /app hashicorp/terraform apply
```

## dockerhub
If the github repository has Dockerfile, the image automatelly is built on dockerhub

### WORKDIR
default is /
If workdir not exist, created automatelly.