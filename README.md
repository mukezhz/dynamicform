# Dynamic Form App

This is the clone of google form

1. clone this repo
```
git clone https://github.com/mukezhz/dynamicform.git

```

## TO EXECUTE THIS APP: PRIMITIVE APPROACH
0. goto dynamicform's backend
``` 
cd dynamicform/
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
3. copy the .env_sample to .env
```
cp .env_sample .env
```

4. update the .env & check the **NOTE:** below

5. create necessary tables
```
python db.py -t all
```

6. to run the project
```
python app.py -p 8000
```

**NOTE:** You need to install mysql and create database before filling into .env

 
### Ways to install mysql:

 1. install [xampp](https://www.apachefriends.org/download.html)
 2. install mysql specific to your operating system
 3. for unix like system install mysql server
    - [for ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
    - [for arch](https://www.vultr.com/docs/how-to-install-mariadb-10-3-or-mysql-8-0-on-arch-linux/)

  For arch:
  ```
  sudo pacman -S mariadb mariadb-clients mariadb-libs
  ```
  
## TO EXECUTE THIS APP: MODERN APPROACH 

### [checked only on docker-compose verion 1.28.* and 2.3.*]

**Please use docker-compose version 1.28.* or +**

---
### No need to install database managent software in your machine

0. goto dynamicform
```
cd dynamicform/
```
1. [Install docker](https://docs/docker.com/get-docker/)
2. [Install docker-compose](https://docs.docker.com/compose/install)

For arch:
```
sudo pacman -S docker docker-compose
```
3. add your `username` in `docker` group. [So that we don't need to use sudo] 
```
sudo usermod -aG docker <your-username>
``` 
4. run docker-compose and viola: [Don't forget to check **NOTE** below]
```
docker-compose up
```
---
5. use api testing tools like postman, insomnia, or curl, or browser

To check:
```
curl http://localhost:8000/api/users/
```

**NOTE**: **DON'T FORGET TO CHANGE YOUR .env** if you are using MODERN APPROACH

`MYSQL_HOST=db` [because: name of my database in `docker-compose` is `db` or change the docker-compose.yml file]

---
**Enjoy your day:** 😋 😋 😋 
