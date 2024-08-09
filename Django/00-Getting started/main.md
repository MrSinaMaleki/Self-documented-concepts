## Getting started with Django

first all you need to do is to start the virtual env with the following command:

```commandline
Python -m venv venv
```
The second venv is pointing at the variables and the second one is the name of our envirnment.
The -m is point at python modules.

Now you need to activate the venv by using a command:

```commandline
source venv/bin/activate.fish
```

```commandline
pip install django
```

```commandline
mkdir mysite
```

```commandline
django-admin startproject config .
```

```commandline
Python manage.py startapp blog
```

```commandline
makemigrations
```

```commandline
migrate
```

You can set Pychram up in a way that can help you alot in the development process.
1. venv auto activate
2. configurations
3. django support

----
Ctrl + Alt + R --> manage.py script

----
Python console ---> Interactive Shell

----

HTML LIVE JIJA AND TDE editors.