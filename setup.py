from setuptools import setup, find_packages

setup(
    name='polis',
    version='0.0',
    py_modules=['polis'],
    install_requires=[
	'click>=5',
        'shapely',
        'fiona',
        'rtree==0.8'
    ],
    entry_points='''
    [console_scripts]
    polis=polis:score
    ''',
)

