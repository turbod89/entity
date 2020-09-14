import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="entity-turbod89",
    version="0.0.1",
    author="turbod89",
    author_email="turbod@localhost",
    description="A library to make python entity models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turbod89/entity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
