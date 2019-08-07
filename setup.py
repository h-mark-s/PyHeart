from setuptools import setup

setup(
    name='pyheart',
    version='0.0.5',
    description='A simple Python3 heartbeat package.',
    py_modules=["pyheart"],
    install_requires=['logging>=0.4.9.6','requests-toolbelt>=0.9.1'],
    package_dir={'': 'src'},
)
