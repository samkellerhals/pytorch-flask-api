from setuptools import setup

setup(
    name='pytorch_flask_api',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)