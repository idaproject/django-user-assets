=============================
Django User Assets
=============================

.. image:: https://badge.fury.io/py/django-user-assets.svg
    :target: https://badge.fury.io/py/django-user-assets

.. image:: https://travis-ci.org/idaproject/django-user-assets.svg?branch=master
    :target: https://travis-ci.org/idaproject/django-user-assets

.. image:: https://codecov.io/gh/idaproject/django-user-assets/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/idaproject/django-user-assets

Allow users to create site assets with django admin

Documentation
-------------

The full documentation is at https://django-user-assets.readthedocs.io.

Quickstart
----------

Install Django User Assets::

    pip install django-user-assets

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django.contrib.sites',
        ...
        'user_assets.apps.UserAssetsConfig',
        ...
    )

Features
--------

1. Add different assets (script, style, e.t.c) to your site from admin panel
2. Place your assets to any place on page with Asset Groups
3. Attach your assets to specific sites from Django Sites Framework

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
