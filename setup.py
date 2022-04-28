#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Kunal Ghosh",
    author_email='kunal.ghosh@aalto.fi',
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
    description="Given PubMed and Arxiv xml dumps, returns a summary",
    entry_points={
        'console_scripts': [
            'academic_stats=academic_stats.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='academic_stats',
    name='academic_stats',
    packages=find_packages(include=['academic_stats', 'academic_stats.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kunalghosh/academic_stats',
    version='0.1.0',
    zip_safe=False,
)
