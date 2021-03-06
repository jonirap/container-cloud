import setuptools

with open("test_requirements.txt", "r") as fh:
    requirements = fh.read()

setuptools.setup(
    name="test-container-cloud",
    version="0.0.1",
    description="Test the container cloud runtime",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8.0",
    install_requires=requirements,
)