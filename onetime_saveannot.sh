#/bin/bash
docker-compose exec cvat python3 manage.py makemigrations downloadlist
docker-compose exec cvat python3 manage.py migrate downloadlist
docker exec -it cvat bash -ic 'python3 ~/manage.py createsuperuser'
