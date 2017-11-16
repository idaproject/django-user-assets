=====
Usage
=====

To use Django User Assets in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'user_assets.apps.UserAssetsConfig',
        ...
    )

Add Django User Assets's URL patterns:

.. code-block:: python

    from user_assets import urls as user_assets_urls


    urlpatterns = [
        ...
        url(r'^', include(user_assets_urls)),
        ...
    ]
