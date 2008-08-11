#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import glob

setup(name='vleech',
      version='0.1',
      description='A video leecher for sites like youtube',
      author='Jan Huelsbergen',
      author_email='jan@afoo.de',
      url='http://github.com/justafoo/vleech/',
      packages=['vleech', 'vleech.siteplugins'],
      scripts=['vleech.py'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: Unix'])
