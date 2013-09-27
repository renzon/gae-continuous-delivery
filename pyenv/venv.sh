#!/bin/bash

set -e  # If occur any error, exit
set -x  # Verbose mode

function to_console {
    echo -e "\n*** $1 ***\n"
}

to_console "Setting up virtualenv on pyenv"

source bin/activate || (virtualenv -p /usr/bin/python2.7 ../pyenv && source bin/activate)

to_console "Checking up dependencies"

pip install -r requirements.txt --upgrade --use-mirrors

to_console "Creating symlink on src/lib so installed libs become visible to Google App Engine"

cd ../src

ln -s ../pyenv/lib/python2.7/site-packages lib



