"""Python setup.py for service_a package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("service_a", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="service_a",
    version=read("service_a", "VERSION"),
    description="Awesome service_a created by CJSmith-0141",
    url="https://github.com/CJSmith-0141/service_A/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="CJSmith-0141",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["service_a = service_a.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
