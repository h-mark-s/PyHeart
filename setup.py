import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='PyHeart',
        version='1.0',
        scripts=['pyheart'],
        description='A simple heartbeat package for Python 3',
        long_description=long_description,
    long_description_content_type='text/markdown',
        url='https://github.com/h-mark-s/pyheart/pyheart'
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language:: Python :: 3',
            'License :: OSI Approved :: MIT License''
            'Operating System :: OS Independent',
        ],
)
