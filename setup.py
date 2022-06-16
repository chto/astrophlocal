#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


requirements = ["requests", "numpy ", "arxivscraper", "pandas", "argparse"]


setup(
    author="Chun-Hao To",
    author_email='chunhaoto@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="arxivlocal",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='astrophlocal',
    name='astrophlocal',
    packages=find_packages(include=['astrophlocal', 'astrophlocal.*', "script"]),
    test_suite='tests',
    url='https://github.com/chto/astrophlocal',
    version='0.0.3',
    zip_safe=False,
)

