# Dynamic Form App

This is the clone of google form

## TO EXECUTE THIS APP:

0. clone this repo
```
git clone https://github.com/mukezhz/dynamicform.git
```

1. install poetry
```
pip install poetry
```

2. install dependencies
```
poetry shell
poetry install
```
3. rename the .env_sample to .env
```
mv .env_sample .env
```

4. update the .env

**NOTE:** You need to install mysql and create database before filling into .env
 
 ### Ways to install mysql:

 1. install [xampp](https://www.apachefriends.org/download.html)
 2. install mysql specific to your operating system
 3. for unix like system install mysql server
    - [for ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
    - [for arch](https://www.vultr.com/docs/how-to-install-mariadb-10-3-or-mysql-8-0-on-arch-linux/)