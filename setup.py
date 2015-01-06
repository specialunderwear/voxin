from setuptools import setup, find_packages


__author__ = "Lars van de Kerkhof <lars@permanentmarkers.nl>"
__version__ = "0.0.1"


setup(
    # package name in pypi
    name='voxin',
    # extract version from module.
    version=__version__,
    description="A tornado example.",
    long_description="Ik heet voxin",
    classifiers=[],
    keywords='',
    author='Lars van de Kerkhof',
    author_email='lars@permanentmarkers.nl',
    url='https://github.dtc.avira.com/VDT/mockengine',
    license='',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples']),
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'distribute',
        'argparse',
        'tornado',
    ],
    # generate scripts
    entry_points={
        'console_scripts': [
            'voxin = voxin.server:main'
        ]
    },
)
