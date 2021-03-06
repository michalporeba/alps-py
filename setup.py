from setuptools import find_packages, setup


def long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setup(
    name="alps-py",
    packages=find_packages(include=["alps"]),
    version="0.2.0",
    author="Michal Poreba",
    license="MIT",
    description="An ALPS library for python",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/michalporeba/alps-py/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    install_requires=["diogi"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
