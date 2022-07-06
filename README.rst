# wallymart

Instructions to run this Project

I have dockerized to freeze the enviornment

```
docker run -p 8080:8080 sirisha7474/wallymart:latest
```

Create Super user
```
docker ps 
docker exec -it DOCKER_ID python manage.py createsuperuser --username siri@siri.com --email siri@siri.com
```