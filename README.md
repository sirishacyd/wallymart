## Project X Alternative [Wallymart]

Wallymart has asked you to take on AmazingCo in the online e-commerce space. Wallymart can't seem to catch up, but they have identified several areas that are crucial to a successful e-commerce site
- high quality customer reviews
- large selection of products
- fast delivery

You know Wallymart does really well in physical in-store space. You also know Wallymart has appetite to radically change the way their e-commerce store is designed today.
You are in the driver seat.

Option #1: Design a web store complete with products, reviews, ordering capabilities, and delivery. You will own this end to end meaning that Wallymart has decided to even own the delivery of the products and not outsource to USPS, UPS, etc.



## Installation


Instructions to run this Project

I have dockerized the e-commerce website to freeze the enviornment so this can be simply run in anywhere.


```
docker run -p 8080:8080 sirisha7474/wallymart:latest
```


Create Super user

```
docker ps
docker ps | grep wallymart | awk '{print  $1 " python manage.py createsuperuser --username siri --email siri@example.com"}' | xargs -o docker exec -it  
```

go to http://localhost:8080

## Develop Locally using python setup

```
virtualenv wallymart
 . ./wallymart/bin/activate
pip install django-oscar sorl-thumbnail
python manage.py migrate
python manage.py runserver
```
go to http://127.0.0.1:8000

Demo Link: https://youtu.be/Zo3a_X4Zfa4
