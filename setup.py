from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'description.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="mtaa",
    version="1.3",
    description="A package consisting of all Tanzania locations from region to streets in a easy accessible way",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Kalebu/mtaa",
    download_url="https://github.com/Kalebu/mtaa/archive/1.3.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["mtaa"],
    keywords=[
        "mtaa",
        "python-tanzania",
        "tanzania locations",
        "mtaa python",
        "mtaa package",
        "mtaa python package",
        "all tanzania location",
        "mtaa github",
        "python mtaa",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
