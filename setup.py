from setuptools import setup

setup(
    name='Walkers',
    version='0.1',
    description='A collection of web crawlers attuned to specific APIs',
    author='J4Numbers',
    author_email='j4numbers@gmail.com',
    packages=['walkers'],
    requires=['requests', 'xmltodict'],
    license='Apache2'
)
