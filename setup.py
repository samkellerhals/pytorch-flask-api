from setuptools import setup

setup(
    name='pytorch_flask_api',
    packages=['torch_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful'
    ],
)