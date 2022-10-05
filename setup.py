#!/usr/bin/env python3

import os
import setuptools


def _read_reqs(relpath):
    fullpath = os.path.join(os.path.dirname(__file__), relpath)
    with open(fullpath) as f:
        return [s.strip() for s in f.readlines()
                if (s.strip() and not s.startswith("#"))]


_REQUIREMENTS_TXT = _read_reqs("requirements.txt")


setuptools.setup(
    name='detic_fork',
    version='0.0.2',
    install_requires=_REQUIREMENTS_TXT,
    include_package_data=True,
    description="Fork of repository https://github.com/facebookresearch/Detic",
    url="https://github.com/nateagr/Detic",
    packages=setuptools.find_packages()
)
