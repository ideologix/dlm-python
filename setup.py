# coding=utf-8

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    name='digital_license_manager',
    version='1.0.0',
    description='Digital License Manager API Client',
    long_description='Python library for working with the Digital License Manager REST APIs',
    url='https://github.com/ideologix/dlm-python',
    author='IDEOLOGIX Media',
    author_email='info@codeverve.com',
    license='GPLv3',
    keywords='digital_license_manager licensing software-licensing license software',

    packages=find_packages(),

    install_requires=[
        'requests'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
