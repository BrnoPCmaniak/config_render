# -*- coding: utf-8 -*-

'''
Created on 28. 8. 2016

@author: Filip Dobrovolný
'''

from setuptools import setup
from config_render import __version__
import os
import io

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name='config_render',
    version=__version__,
    platforms=['OS Independent'],
    description='Render your config files automaticly with Jinja2.',
    # long_description=read('README.txt', 'CHANGES.txt'),
    keywords='jinja2 config',
    url='https://github.com/BrnoPCmaniak/config_render',
    author='Filip Dobrovolny',
    author_email='brnopcman@gmail.com',
    license='MIT',
    maintainer='Filip Dobrovolny',
    maintainer_email='brnopcman@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Installation/Setup',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['config_render'],
    scripts=['scripts/config_render'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2',
    ],
)
