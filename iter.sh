#!/bin/bash

echo -e 'y\n' | pip uninstall offlinedoc
rm -f dist/*
python setup.py sdist
pip install dist/*.gz
