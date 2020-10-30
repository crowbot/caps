#!/bin/bash

# abort on any errors
set -e

# check that we are in the expected directory
cd `dirname $0`/..

virtualenv_args=""
virtualenv_dir='../venv'
virtualenv_activate="$virtualenv_dir/bin/activate"
if [ ! -f "$virtualenv_activate" ]
then
    python3 -m venv $virtualenv_dir
fi
source $virtualenv_activate

pip3 install --requirement requirements.txt

# make sure that there is no old code (the .py files may have been git deleted)
find . -name '*.pyc' -delete

# get the database up to speed
python3 manage.py migrate

mkdir -p data/plans
