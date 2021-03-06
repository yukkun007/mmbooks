import os
from setuptools import setup

PACKAGE_NAME = "mmbooks"

with open("README.md") as f:
    readme = f.read()

with open(os.path.join(PACKAGE_NAME, "VERSION")) as f:
    version = f.read()

setup(
    # matadata
    name=PACKAGE_NAME,
    version=version,
    description="my book service library",
    long_description=readme,
    author="Yutaka Kato",
    author_email="kato.yutaka@gmail.com",
    url="https://github.com/yukkun007/mmbooks",
    # liscence=
    # platform=
    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[],
    entry_points="""
        [console_scripts]
        {app} = {app}.cli:main
    """.format(
        app=PACKAGE_NAME
    ),
)
