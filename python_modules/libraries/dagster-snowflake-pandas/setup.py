from typing import Dict

from setuptools import find_packages, setup


def get_version() -> str:
    version: Dict[str, str] = {}
    with open("dagster_snowflake_pandas/version.py", encoding="utf8") as fp:
        exec(fp.read(), version)  # pylint: disable=W0122

    return version["__version__"]


if __name__ == "__main__":
    ver = get_version()
    # dont pin dev installs to avoid pip dep resolver issues
    pin = "" if ver == "0+dev" else f"=={ver}"
    setup(
        name="dagster-snowflake-pandas",
        version=ver,
        author="Elementl",
        author_email="hello@elementl.com",
        license="Apache-2.0",
        description="Package for integrating Snowflake and Pandas with Dagster.",
        url="https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-snowflake-pandas",
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        packages=find_packages(exclude=["dagster_snowflake_pandas_tests*"]),
        install_requires=[
            f"dagster{pin}",
            f"dagster-snowflake{pin}",
            "pandas",
            "requests",
            "snowflake-connector-python[pandas]",
            "snowflake-sqlalchemy",
        ],
        zip_safe=False,
    )
