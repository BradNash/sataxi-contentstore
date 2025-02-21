import setuptools
import sys

number_of_arguments = len(sys.argv)
version_parameter = sys.argv[-1]
version = version_parameter.split("=")[1]
sys.argv = sys.argv[0 : number_of_arguments - 1]

setuptools.setup(
    name="sataxi.contentstore.messaging",
    version=version,
    author="BBD",
    author_email="nicholasp@bbd.co.za",
    description="SaTaxi Content Store messages package",
    long_description="SaTaxi Content Store messages package",
    long_description_content_type="text/markdown",
    url="https://git-codecommit.eu-west-1.amazonaws.com/v1/repos/bbd-services-contentstore",
    platforms="any",
    package_dir={"sataxi": "src/python/sataxi"},
    packages=[
        "sataxi.contentstore.messaging.commands",
        "sataxi.contentstore.messaging.events",
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: BBD",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    install_requires=[
        "bbd.libs.python>=3.3.13",
    ],
    setup_requires=[
        "wheel",
    ],
)
