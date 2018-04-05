#!/bin/bash

# runs the auth-generator script whenever the source csv changes
#
# requirements:
#  * ruby
#  * entr (http://entrproject.org)

PROJECT_ROOT=$HOME/Projekte/ckanext-berlinauth
GENERATOR_SCRIPT=$PROJECT_ROOT/auth-generator/auth-generator.rb
PLUGIN_SOURCE=$PROJECT_ROOT/ckanext/berlinauth/plugin.py

# watch the source CSV and run the generator script when it changes

ls $1 | entr ruby $GENERATOR_SCRIPT $1 $PLUGIN_SOURCE BerlinauthPlugin