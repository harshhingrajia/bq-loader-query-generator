from setuptools import setup, find_packages

setup(
    name="bq-query-generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "jinja2",
    ],
    entry_points={
        'console_scripts': [
            'bq-query-generator = cli.generate_sql:main',
        ],
    },
)
