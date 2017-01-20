

from setuptools import setup

setup(name='twitterToy',
      version='0.1',
      packages=['modules', 'database'],
      license='MIT',
      description='Abstractions on Twitter API',
      install_requires=['networkx', 'python-twitter', 'matplotlib', 'unittest'],
      author='Nicholas Clement',
      author_email='nicholas.clement@colorado.edu',
      url='N.A.',
     )
