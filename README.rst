===============
Image Inspector
===============


.. image:: https://img.shields.io/pypi/v/image_inspector.svg
        :target: https://pypi.python.org/pypi/image_inspector

.. image:: https://img.shields.io/travis/TNRIS/image_inspector.svg
        :target: https://travis-ci.org/TNRIS/image_inspector

.. image:: https://readthedocs.org/projects/image-inspector/badge/?version=latest
        :target: http://image-inspector.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/TNRIS/image_inspector/shield.svg
        :target: https://pyup.io/repos/github/TNRIS/image_inspector/
        :alt: Updates


Command line utility to export exif data to a csv.


* Free software: MIT license
* Documentation: https://image-inspector.readthedocs.io.


Features
========

* Iterates through a base directory to find .tif files.
* Outputs a CSV of EXIF tags for each .tif file.
* User can specify only a set list of tags to capture.

Usage
=====

Basic Usage:

.. code-block:: console

    $ image-inspector .

Specifying a Directory:

.. code-block:: console

    $ image-inspector /test/sample_images

Filtering Exported Fields:

.. code-block:: console

    $ image-inspector . "Image XResolution" "Image YResolution"

User-defined Output File:

.. code-block:: console

    $ image-inspector . --inventory-file-name "images_2016"

Overwrite Existing Inventory Files:

.. code-block:: console

    $ image-inspector . --overwrite

Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

