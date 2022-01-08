from setuptools import setup, find_packages

setup(
    name='stock_price_alerting',
    packages=find_packages(where='./src'),
    package_dir={
        '': 'src',
    },
    description='My project to be packaged',
    version='1.0.0',
    author='johnmu'
)
