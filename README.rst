=================
django-audioadmin
=================

A reusable Django app for uploading/previewing audio files with a simple id3 tag reader.


.. image:: https://github.com/ngrinkevich/django-audioadmin/raw/master/docs/images/audioadmin.gif


Installation
============
* Requires Django 1.7 or greater

* Install from PyPi with pip::
    
    pip install django-audioadmin
    

* Add ``"audioadmin"`` to the ``INSTALLED_APPS`` in your ``settings.py``::

    INSTALLED_APPS = (
        ...
        "audioadmin"
        ...
    )

* Make sure you have your Media folder setup. Add these to your ``settings.py``::

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

* Make sure your media files can be served on dev. Add these to your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^admin/', include(admin.site.urls)),
        ...             
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

* Run migrations::

    ./manage.py migrate

* Start development server::

    ./manage.py runserver

* To run tests::

    ./manage.py test

Credits
=======

* Audio playback is provided by `SoundManager2 <http://www.schillmania.com/projects/soundmanager2/>`_


License
=======

Django-Audioadmin is licensed under MIT, see `MIT-LICENSE.txt`.
