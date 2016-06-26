# Entries
## Projektről

Ez egíy gyüjtő weblap a BME-s hallagtóként ingyenesen elérhető prémium szolgáltatásokról.
A Github studentpack-hez hasnolóan.

## Függöségek
- python3
- django == 1.9.5
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
