from setuptools import setup

setup(
    name="pycat",
    version="0.1",
    description="a quick pure-Python version of netcat",
    url="https://github.com/loganjameshart/pytemplate",
    author="Logan James Hart",
    author_email="logan@loganjameshart.com",
    license="MIT",
    py_modules=["pycat"],
    entry_points={
        "console_scripts": [
            "pycat = pycat:main",
        ]
    },
)
