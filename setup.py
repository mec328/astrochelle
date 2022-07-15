from setuptools import setup, find_packages

from astrochelle.__init__ import __version__

setup(
    name='astrochelle',
    version=__version__,

    url='http://github.com/mec328/astrochelle',
    author='Michelle Chernick',
    author_email='mcparakeet@gmail.com',

    packages=find_packages(),
)