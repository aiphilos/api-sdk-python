import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiphilos",
    version="0.0.1",
    author="aiPhilos",
    author_email="mail@aiphilos.com",
    description="aiPhilos API Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://aiphilos.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)