import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsolver",
    version="0.0.1",
    author="Shivam Agrawal",
    author_email="shivam301296@gmail.com",
    description="Resolve Python dependencies automatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivampip/DSolver",
    packages=setuptools.find_packages(),
    install_requires=[
          'colorlog',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)