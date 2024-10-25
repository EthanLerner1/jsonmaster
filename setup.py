from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def read_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


setup(
    name="jsonmaster",
    version="1.0.1",
    author="Ethan Lerner",
    author_email="lerner.ethan@gmail.com",
    description="A Python package for making your life of working with json's, easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EthanLerner1/jsonmaster",
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    extras_require={
        "dev": ["pytest"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
