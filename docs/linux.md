# VM init for CentOS 7
## local machine

### copy private key
```
scp ~/.ssh/id_rsa ${target_machine}:~/.ssh/
```

## VM (Cent OS)
### set swap
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
