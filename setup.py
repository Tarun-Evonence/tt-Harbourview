# setup.py
from setuptools import setup, find_packages

setup(
    name='pythonwheel',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'pythonwheel = pythonwheel.__main__:main',
        ],
    },
)
