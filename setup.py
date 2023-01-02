from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aurora",
    version="0.0.1",
    author="Laurindo Diniz",
    author_email='lrnddiniz@gmail.com',
    description="Plot simple and elegant graphs for daily data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["aurora"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['seaborn==0.12.2',
                      'matplotlib==3.6.0'],
    dependency_links=['https://github.com/laurindo-diniz/aurora']
)