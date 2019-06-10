# dollarBackend

This project uses docker

To build the image
```bash
docker-compose build
```

To raise the backend docker


```bash
docker-compose up
```


if it is the first time the program runs

it is necessary to populate the database
```
docker exec -it dollar_backend python /www/manage.py populate all
```
