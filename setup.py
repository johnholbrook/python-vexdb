import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vexdb",
    version="1.0.15",
    author="John Holbrook",
    author_email="contact@johnholbrook.us",
    description="A thin python wrapper for the vexDB API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dhmmjoph/python-vexdb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)