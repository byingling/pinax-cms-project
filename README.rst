===========
CMS Project
===========

This repository stores the Django-CMS starter project for Pinax. 
This project is open source and the license can be found in LICENSE.


Installation
============

To get setup with cms_project code you must have the following
installed:

 * Python 2.6+
 * virtualenv 1.4.7+
 * C compiler (for PIL)

Setting up environment
----------------------

Create a virtual environment where your dependencies will live::

    $ virtualenv --no-site-packages mycmsproject
    $ source mycmsproject/bin/activate
    (mycmsproject)$ pip install pinax

Use cms_project as your project.

OR

Copy package to site-packages/ directory and setup new project::

    (mycmsproject)$ pinax-admin setup_project -b cms mycms

Setting up the database
-----------------------

This will vary for production and development. By default the project is set
up to run on a SQLite database. If you are setting up a production database
see the Configuration section below for where to place settings and get the
database running. Now you can run::

    (mycmsproject)$ python manage.py syncdb

Running a web server
--------------------

In development you should run::

    (mycmsproject)$ python manage.py runserver

For production, this project comes with a WSGI entry point located in
``deploy/wsgi.py`` and can be referenced by gunicorn with
``deploy.wsgi:application``.

Configuration
=============

You can create a ``local_settings.py`` file alongside ``settings.py`` to
override any setting that may be environment/instance specific. This file is
ignored in ``.gitignore``.
