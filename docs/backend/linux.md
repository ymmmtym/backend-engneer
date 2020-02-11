# Linux
## Makefile
ex)

```Makefile
makemigrations:
    docker-compose run --rm web python3 manage.py makemigrations

migrate:
    docker-compose run --rm web python3 manage.py migrate

createsuperuser:
    docker-compose run --rm web python3 manage.py createsuperuser
```

## VM init for CentOS 7
### Copy private key from local machine
```
scp ~/.ssh/id_rsa ${target_machine}:~/.ssh/
```

### setting swap
```
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo sed -i '$ a /swapfile                                 swap                    swap    defaults        0 0' /etc/fstab
```

### update yum repository
```
sudo yum update
```

## Other
show hardware info

```
dmidecode
```

grep without reg exspression

```
grep -F 'hoge' sample.txt
fgrep 'hoge' sample.txt
```

vimdiff
- do
- dp
- :wqa
- :xa

tree

```
tree  --charset=C
```