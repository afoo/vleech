#!/bin/sh
python setup.py clean -a
[ -d dist ] && rm -r dist
fakeroot debian/rules clean
