import os
import sys
from codecs import open

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass into pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = "-n auto"

    def run_tests(self):
        import shlex

        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="telnyx",
    version="2.1.2",
    description="Python bindings for the Telnyx API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Telnyx",
    author_email="support@telnyx.com",
    url="https://github.com/team-telnyx/telnyx-python",
    project_urls={
        "Documentation": "https://developers.telnyx.com/docs/api/v2/overview",
        "Source Code": "https://github.com/team-telnyx/telnyx-python",
        "Bug Tracker": "https://github.com/team-telnyx/telnyx-python/issues",
    },
    license="MIT",
    keywords="telnyx telephony sip networking callcontrol messaging sms mms",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=[
        "requests >= 2.20",
        "six",
        "PyNaCl",
        "black",
    ],
    python_requires=">=3.8",
    tests_require=[
        "pytest >= 4",
        "pytest-mock >= 1.7",
        "pytest-xdist >= 1.22",
        "pytest-cov >= 2.5",
    ],
    cmdclass={"test": PyTest},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications :: Telephony",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
