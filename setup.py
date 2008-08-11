#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='vleech',
      version='0.1',
      description='A video leecher for sites like youtube',
      author=u'Jan Hülsbergen',
      author_email='jan@afoo.de',
      packages=('vleech',),
      scripts=('src/vleech.py',))
