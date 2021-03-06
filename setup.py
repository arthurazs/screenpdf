#!/usr/bin/env python3
# coding: utf-8
from setuptools import setup
import os.path as path


info_name = 'screenpdf'
info_url = 'https://github.com/arthurazs/{}/'.format(info_name)
author_name = 'Arthur Zopellaro'
email = 'arthurazsoares@gmail.com'

try:
    with open(path.abspath(path.join(info_name,
                                     'version.py'))) as version:
        exec(version.read())
except IOError:
    print('ERROR version not found')
    __version__ = ''

info_download = '{}archive/v{}.tar.gz'.format(info_url, __version__)

try:
    with open('PyPIREADME.rst', 'r') as readme:
        info_long_description = readme.read()
except IOError:
    try:
        print(
            'PyPIREADME.rst not found, trying '
            'README.md instead')
        print(
            'WARNING It isn\'t recommended to upload '
            'a markdown file as README to PyPI')
        with open('README.md', 'r') as readme:
            info_long_description = readme.read()
    except IOError:
        print('ERROR README.md not found either')
        info_long_description = ''


setup(
    name=info_name,
    version=__version__,
    author=author_name,
    author_email=email,
    maintainer=author_name,
    maintainer_email=email,
    description=(
        '{} converts *.spdf to proper screenplay'
        ' PDF format.'.format(info_name)),
    license='MIT',
    keywords=(
        'script screenplay format formatter'
    ),
    url=info_url,
    download_url=info_download,
    packages=[info_name],
    package_data={
        info_name: [
            'templates/*', 'data/*']},
    long_description=info_long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities'
    ],
    setup_requires=['setuptools', 'pip', 'nose', 'rednose'],
    install_requires=['fpdf'],  # try fpdf2 in the future
    entry_points={
        'console_scripts': [
            '{0}={0}.__main__:main'.format(info_name)]
    },
    tests_require=['nose', 'rednose', 'tox'],
    test_suite='nose.collector'
)
