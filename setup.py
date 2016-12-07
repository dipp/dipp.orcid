#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '0.1'

def _read(doc):
    return open(doc, 'rb').read()

setup(name='dipp.orcid',
      version=__version__,
      description="access orcid restful webservice",
      long_description=_read('README.rst').decode('utf-8'),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Peter Reimer',
      author_email='reimer@hbz-nrw.de',
      url='',
      license='DFSL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dipp', 'dipp.orcid'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Requests',
          # -*- Extra requirements: -*-
      ],
     entry_points={
        'console_scripts':[
            'orcid=dipp.orcid.orcid:main',
          ]  
     },
     )
