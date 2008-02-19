from setuptools import setup, find_packages
from os import sep
from os.path import curdir

version = '0.1'

long_description = open(sep.join((curdir, 'src','megrok','form','README.txt'))).read()

setup(name='megrok.form',
      version=version,
      description="Fields, Widgets and Constraints for Grok",
      long_description=long_description,
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Zope Public License',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent',
                   'Topic :: Internet :: WWW/HTTP',
                   ],
      keywords="grok form widgets fields constraints",
      author="Dirceu Pereira Tiegs",
      author_email="dirceutiegs@gmail.com",
      url="http://svn.zope.org/Sandbox/dirceu/megrok.form",
      license="ZPL",
      package_dir={'': 'src'},
      namespace_packages=['megrok'],
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'zc.resourcelibrary',
                        'z3c.widget',
                        'zc.datetimewidget',
                        'collective.namedfile',
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
