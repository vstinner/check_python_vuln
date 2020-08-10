*****************
check_python_vuln
*****************

.. image:: https://img.shields.io/pypi/v/check_python_vuln.svg
   :alt: Latest release on the Python Cheeseshop (PyPI)
   :target: https://pypi.python.org/pypi/check_python_vuln

.. image:: https://travis-ci.com/vstinner/check_python_vuln.svg?branch=master
   :alt: Build status of check_python_vuln on Travis CI
   :target: https://travis-ci.com/github/vstinner/check_python_vuln

Check for Python vulnerabilities.

Homepage: https://github.com/vstinner/check_python_vuln

Support Python 2.7 and Python 3.6 to 3.10.

See `Python Security Vulnerabilities
<https://python-security.readthedocs.io/>`_.


Usage
=====

Check for vulnerabilities::

    python3 -m check_python_vuln


Run tests
=========

Command to run tests::

    tox --parallel auto


Changelog
=========

* 2020.07.01.post1: Install data files and support Python 2.7 older than 2.7.9.
* 2020.07.01: Initial release.
