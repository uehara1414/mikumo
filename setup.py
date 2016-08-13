import os
from setuptools import setup


long_description = """Python wrapper for ConoHa API"""

if os.path.isfile("README.md"):
    with open('README.md') as file:
        long_description = file.read()

setup(
    name='mikumo',
    version='0.1.0',
    description="""Python wrapper for ConoHa API""",
    author='uehara1414',
    author_email='akiya.noface@gmail.com',
    url='https://github.com/uehara1414/mikumo',
    packages=['mikumo'],
    install_requires=['requests'],
    license='MIT',
    long_description=long_description
)
