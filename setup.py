import re
from setuptools import setup, find_packages

_version_re = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'

with open('requests/__init__.py', 'r') as f:
    version = re.search(_version_re, f.read(), re.MULTILINE).group(1)

setup(
    name='requests-login',
    version=version,
    packages=find_packages(),
    install_requires=['requests>=2.11.0'],

    author='jxltom',
    author_email='jxltom@gmail.com',
    license='MIT',
    keywords='login requests cookies forum discuz',
    url='https://github.com/jxltom/requests-login/',
    description='Simple way for logging in any forums or websites '
                'based on requests',
)
