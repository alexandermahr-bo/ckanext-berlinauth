#! /bin/bash

export CKAN_INI="/usr/lib/ckan/default/src/ckan/test-core.ini"

# delete .pyc-files to prevent the "import file mismatch" errors
find -name "*.pyc" -delete
# coverage run --source=ckanext.berlinauth -m pytest -vv --log-cli-level=10 ckanext/berlinauth/tests -k "$1" && coverage html
coverage run --source=ckanext.berlinauth -m pytest ckanext/berlinauth/tests -k "$1" && coverage html
