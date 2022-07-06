#wallymart

Instructions to run this Project

I have dockerized the e-commerce website to freeze the enviornment

````
docker run -p 8080:8080 sirisha7474/wallymart:latest
````

Create Super user

````
docker ps 
docker exec -it DOCKER_ID python manage.py createsuperuser --username johndoe --email johndoe@example.com
````
