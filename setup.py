from setuptools import setup, find_packages
import os

version = '0.1'

tests_require = [
    'pytest',
    'pytest-cov',
]

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
AUTHORS = open(os.path.join(here, 'AUTHORS.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

long_description = (
    README
    + '\n' +
    AUTHORS
    + '\n' +
    CHANGES
)

setup(name='kotti_software',
      version=version,
      description="Kotti software",
      long_description=long_description,
      classifiers=[],
      keywords='kotti software',
      author='geojeff',
      author_email='geojeff@me.com',
      url='http://pypi.python.org/pypi/kotti_software',
      license=' BSD-derived (http://www.repoze.org/LICENSE.txt)',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Kotti>=0.7',
          'plone.batching',
          'AccessControl',  # this is actually a dependency of plone.batching
          'js.jquery_infinite_ajax_scroll',
          'python-dateutil',
      ],
      project_points="""
      [fanstatic.libraries]
      kotti_software = kotti_software:library
      """,
      tests_require=tests_require,
      extras_require={
          'testing': tests_require,
          },
      message_extractors={'kotti_software': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )