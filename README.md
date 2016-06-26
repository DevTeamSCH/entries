# Entries
## Projektről

Ez egy gyüjtő weblap a BME-s hallagtóként ingyenesen elérhető prémium szolgáltatásokról.
A Github studentpack-hez hasnolóan.

## Függöségek
- python3 >= 3.4
- django >= 1.9, <1.10
- django-rosetta
- pillow
- bower
- jquery
- uikit
- sass

## Telepítés

````pip install -r requirements.txt````

````bower install````

````sassc static/sass/base.sass static/css/base.css````

````./manage.py compilemessages````

````./manage.py migrate````

````./manage.py runserver````
