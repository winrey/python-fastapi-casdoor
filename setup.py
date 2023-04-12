#!/usr/bin/python
# encoding: utf-8

from setuptools import setup, find_packages
 
setup(
    name="fastapi-casdoor",
    version="0.1.1",
    python_requires='>=3.10.0',
    license="MIT Licence",
    long_description="Integration Casdoor with FastAPI",
 
    url="https://github.com/winrey/python-fastapi-casdoor",
    author="winrey",
    author_email="i@iaside.com",
 
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
      "fastapi[all] >= 0.95.0",
      "python-dateutil >= 2.8.2",
      "pyjwt >= 2.0.0",
      "pydantic >= 1.10.0",
    ]
)
