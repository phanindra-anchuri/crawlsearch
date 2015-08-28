from setuptools import setup

setup(name='crawler', version='1.0', test_suite='nose.collector', tests_require=['nose'],
      install_requires=['beautifulsoup4', 'reppy'])
