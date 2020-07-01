#!/usr/bin/env python3

# Prepare a release:
#
#  - git pull --rebase
#  - update version in check_python_vuln/__init__.py
#  - Update changelog in README.rst
#  - git commit -a -m "prepare release x.y"
#  - Remove untracked files/dirs: git clean -fdx
#  - run tests: tox --parallel auto
#  - git push
#  - check Travis CI status:
#    https://travis-ci.org/vstinner/check_python_vuln
#
# Release a new version:
#
#  - Remove untracked files/dirs: git clean -fdx
#  - git tag VERSION
#  - python3 setup.py sdist bdist_wheel
#  - git push --tags
#  - twine upload dist/*

from check_python_vuln import __version__

DESCRIPTION = 'Check for Python vulnerabilities'
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
]


def main():
    from setuptools import setup
    import os.path
    import io

    with io.open('README.rst', encoding="utf-8") as fp:
        long_description = fp.read().strip()

    data_dir = os.path.join('check_python_vuln', 'data')
    data_files = [os.path.join('data', name)
                  for name in os.listdir(data_dir)]

    options = {
        'name': 'check_python_vuln',
        'version': __version__,
        'license': 'MIT license',
        'description': DESCRIPTION,
        'long_description': long_description,
        'url': 'https://github.com/vstinner/check_python_vuln',
        'author': 'Victor Stinner',
        'author_email': 'vstinner@redhat.com',
        'classifiers': CLASSIFIERS,
        'packages': ['check_python_vuln'],
        'package_data': {'check_python_vuln': data_files},
    }
    setup(**options)


if __name__ == '__main__':
    main()
