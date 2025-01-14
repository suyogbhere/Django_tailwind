1) python --version   ( Python 3.12.0 )
2) pip --version   ( pip 24.2  )
3) Install the django-tailwind package via pip:
    - python -m pip install django-tailwind
4) Add 'tailwind' to INSTALLED_APPS in settings.py:
    - INSTALLED_APPS = ['tailwind', ]
5) Install node    check   node --version ( v22.13.0 )
6) check npm --version  ( 10.9.2 )

7) Create a Tailwind CSS compatible Django app, I like to call it theme:
    - python manage.py tailwind init
8) Add your newly created 'theme' app to INSTALLED_APPS in settings.py:
    - INSTALLED_APPS = [ 'tailwind', 'theme' ]
9) Register the generated 'theme' app by adding the following line to django settings.py file:
   - TAILWIND_APP_NAME = 'theme'
10) Make sure that the INTERNAL_IPS list is present in the settings.py file and contains the 127.0.0.1 ip address:
    - INTERNAL_IPS = [
    "127.0.0.1", ]
11) Install Tailwind CSS dependencies, by running the following command:
    - python manage.py tailwind install
12) python -m pip install django-browser-reload
    - INSTALLED_APPS = ['tailwind','theme', 'django_browser_reload' ]
13) Staying in settings.py, add the middleware:
    - MIDDLEWARE = [   "django_browser_reload.middleware.BrowserReloadMiddleware", ]
14) Include django_browser_reload URL in your root url.py:
    - from django.urls import include, path
        urlpatterns = [
            path("__reload__/", include("django_browser_reload.urls")),
        ]
15) python manage.py tailwind start    ( to start tailwind css in another terminal)
16) where npm     (to check npm path)
    - NPM_BIN_PATH = '//usr//local//bin//npm'              (# Add npm path in settings.py )