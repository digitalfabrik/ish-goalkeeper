#!/usr/bin/env python3
"""
Install with dependencies
"""

import os
from setuptools import find_packages, setup

setup(
    name="ish-goalkeeper",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={'':'src'},
    include_package_data=True,
    scripts=['src/manage.py'],
    install_requires=[
        "django-mptt",
        "django-filer",
        "django-summernote",
        "matplotlib",
        "django-admin-rangefilter"
    ],
    tests_require=[
        "django-pylint"
    ],
    author="Tuer an Tuer - Digitalfabrik gGmbH",
    author_email="info@integreat-app.de",
    description="Managing ISH courses",
    license="GPL-2.0-or-later",
    keywords="Django In Safe Hands",
    url="http://github.com/Digitalfabrik/ish-goalkeeper/",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
