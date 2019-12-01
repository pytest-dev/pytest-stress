=============
Pytest-stress
=============

.. image:: https://travis-ci.com/pytest-dev/pytest-stress.svg?branch=master
    :target: https://travis-ci.com/pytest-dev/pytest-stress
    :alt: See Build Status on Travis CI

.. image:: https://img.shields.io/pypi/v/pytest-stress.svg
    :target: https://pypi.org/project/pytest-stress
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-stress.svg
    :target: https://pypi.org/project/pytest-stress
    :alt: Python versions

A plugin that allows you to loop tests for a user-defined amount of time.

Requirements
------------

Only tested with `Pytest`_ version 5.2.2.


Installation
------------

You can install "pytest-stress" via `pip`_ from `PyPI`_ (highly recommend installing in a `Pipenv`_)::

$ pip3 install pytest-stress

Usage
-----

Loop tests for 30 seconds::

    $ pytest --seconds 30

Loop tests for 45 minutes::

    $ pytest --minutes 45

Loop tests for 8 hours::

    $ pytest --hours 8

Loop tests for 1 hour 8 minutes and 9 seconds::

    $ pytest --hours 1 --minutes 8 --seconds 9

Need to wait some time after each test loop? Don't say I don't love you::

    $ pytest --delay 5 --hours 4 --minutes 30

You can also add these values to config files::

    [pytest]
    addopts = --hours 1 --minutes 30

Note: These loop times include setup and teardown operations as well. So if you have a test setup that takes 5
seconds, your actual tests will run for 5 seconds less than your desired time.

Contributing
------------
Contributions are very welcome! Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-stress" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

____

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/ImXron/pytest-stress/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`pipenv`: https://pypi.org/project/pipenv/
.. _`PyPI`: https://pypi.org/project
