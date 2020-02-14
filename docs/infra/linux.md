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
```shell
scp ~/.ssh/id_rsa ${target_machine}:~/.ssh/
```

### setting swap
```shell
sudo dd if=/dev/zero of=/swapfile bs=1M count=1024
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo sed -i '$ a /swapfile                                 swap                    swap    defaults        0 0' /etc/fstab
```

### update yum repository
```shell
sudo yum update
```

## Commands
### dmidecode
show hardware info
```shell
dmidecode
```

### grep
without reg exspression
```shell
grep -F 'hoge' sample.txt
fgrep 'hoge' sample.txt
```

### vim
start diff mode

```shell
vimdiff
# or
vim -d
```

commands

```
do # diff obtain
dp # diff put
:wqa # save all and finish
:xa # save all and finish
```

### tree
```
tree  --charset=C
```

### less
```shell
less +F README.md LICENSE
# ^C general mode
# F  monitoring mode
# :n move next file
```

### diff
```shell
diff <($cmd1) <($cmd2)
```

### find
```
find . -name ".sh" -type f exec chmod 755 {} +
```

### mdfind
for MacOS command.

```shell
mdfind -onlyin . ".md"
```