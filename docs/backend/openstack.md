# Openstack
## show uploaded image list

```
openstack image list
cinder image-list
```

## create user

```
openstack user create opcel
openstack user set --password secret opcel
openstack project create proj01
openstack role add --user opcel --project proj01 member
```
