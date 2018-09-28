OMERO.shrtn
===========

OMERO.web app for adding short URLs to OMERO.web.

Short URLs are configured by creating MapAnnotations in a special namespace where keys are the short URL and values are the destination URL.


Requirements
============

* OMERO.web 5.4.0 or newer.


Installation
============

This section assumes that an OMERO.web is already installed.

Install the app from this repository.

Add ``omero_shrtn`` to your installed web apps:

::

    $ bin/omero config append omero.web.apps '"omero_shrtn"'

Now restart OMERO.web as normal.


Usage
=====

Create MapAnnotations (key-value pairs) in the namespace ``openmicroscopy.org/omero/web/shrtn``.
For example key:``look-at-this`` value:``/webclient/?show=image-1`` will create a redirect from ``http://localhost/shrtn/look-at-this`` to ``http://localhost/webclient/?show=image-1``.
Full URLs are allowed e.g. value:``https://www.openmicroscopy.org/``.


Configuration
=============

OMERO.shrtn can be configured to query a different namespace. For example to query MapAnnotations in the default client-editable namespace:

::

    $ bin/omero config set omero.web.shrtn.namespace openmicroscopy.org/omero/client/mapAnnotation

The ``shrtn`` prefix can also be configured.

::

    $ bin/omero config set omero.web.shrtn.prefix s

would make ``http://localhost/s/`` the base for all shortened URLs


**Warning**:

This application should only be installed on servers where all users are trusted. An untrusted user could setup a redirect to a malicious website.


License
-------

OMERO.shrtn is released under the AGPL.

Copyright
---------

2018, The Open Microscopy Environment
