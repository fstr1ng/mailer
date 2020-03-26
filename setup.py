from setuptools import setup, find_packages
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='mailer',
    version='0.0.1',
    description=('Simple Mailer'),
    long_description=long_description,
    author='Mike',
    author_email='inbox@example.com',
    url='https://github.com/author/repo',
    license='MPL-2.0',

    packages=find_packages(),
    include_package_data=True,

#    install_requires=[
#        'dependency==1.2.3',
#    ],

#    scripts=['bin/a-script'],

    entry_points='''
        [console_scripts]
        mailer=mailer.__main__:main
    ''',

    classifiers=[
        'Development Status :: 1 - Planning',
#        'Development Status :: 2 - Pre-Alpha',
#        'Development Status :: 3 - Alpha',
#        'Development Status :: 4 - Beta',
#        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.8'
    ],
)
