OMERO.idirector
===============

OMERO.web app for automatically redirecting based on partial matches on OMERO object names.


Requirements
============

* OMERO.web 5.4.0 or newer.


Installation
============

This section assumes that an OMERO.web is already installed.

Install the app from this repository.

Add ``omero_idirector`` to your installed web apps:

::

    $ bin/omero config append omero.web.apps '"omero_idirector"'

Now restart OMERO.web as normal.


Configuration
=============

For example, to automatically redirect /idr/NNNN projects or screens with names beginning `idr-NNNN-`

::

    $ omero config set omero.web.idirector.prefix idr
    $ omero config set omero.web.idirector.types '["Project", "Screen"]'
    $ omero config set omero.web.idirector.validre '\d{4}$'
    $ omero config set omero.web.idirector.match 'idr{u}-%'


Release process
---------------

Use `bumpversion
<https://pypi.org/project/bump2version/>`_ to increment the version, commit and tag the repo.

::

    $ bumpversion patch
    $ git push origin master
    $ git push --tags


License
-------

OMERO.idirector is released under the AGPL.

Copyright
---------

2018, The Open Microscopy Environment
