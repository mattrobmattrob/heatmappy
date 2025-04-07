from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='heatmappy-bks',
    packages=['heatmappy-bks'],
    version='0.3.0',
    description='Draw image heatmaps in python',
    author='Lumen Research',
    author_email='development@lumen-research.com',
    url='https://github.com/mattrobmattrob/heatmappy',
    keywords=['image', 'heatmap', 'heat map'],
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    include_package_data=True,
)
