# docker
## install for centos
```
sudo yum -y update
sudo yum -y install git docker docker-compose
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo systemctl restart docker
```

## init setting
delete sudo authority for docker cmd
```
sudo groupadd docker
sudo gpasswd -a $USER docker

exit
```

## operation
copy
```
docker cp ${container_id}:${dir} ${output_dir}
```

prune unused containers and images
```
docker system prune
```
