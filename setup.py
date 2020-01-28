#!/usr/bin/env python
from setuptools import find_packages, setup


project = "slice"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="Application to Order Pizzas",
    author="Globality Engineering",
    author_email="engineering@globality.com",
    url="https://github.com/globality-corp/pizza_app",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "microcosm>=2.12.0",
        "microcosm-flask[metrics,spooky]>=1.20.0",
        "microcosm-logging>=1.3.0",
        "microcosm-postgres>=1.19.0",
        "microcosm-secretsmanager>=1.1.0",
        "pyOpenSSL>=18.0.0",
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    entry_points={
        "console_scripts": [
            "createall = slice.main:createall",
            "migrate = slice.main:migrate",
            "runserver = slice.main:runserver",
        ],
    },
    extras_require={
        "test": [
            "coverage>=4.0.3",
            "PyHamcrest>=1.9.0",
        ],
    },
)
