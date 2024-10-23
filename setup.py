from setuptools import setup

setup(
    name="etl_query_tool",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "requests",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "etl_query_tool=main:main",
        ],
    },
    python_requires=">=3.7",
    description="A command-line tool for ETL and database queries.",
    author="Your Name",
    url="https://github.com/nogibjj/py_script_with_SQLDatabase_CLI",
)
