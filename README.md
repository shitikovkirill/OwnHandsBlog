Blog-For-Fiend
-------

### Script for start:
rename local_settings_example.py to local_settings.py
```bash
    docker-compose up
    docker-compose run --rm  web python manage.py createsuperuser
```