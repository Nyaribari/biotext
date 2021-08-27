from setuptools import setup

setup(
name='biotext',
version='0.0.3',
description = 'The package is a text labeling function.',
url = 'git+ssh://git@github.com/Nyaribari/biotext#egg=t_bios',
author='Nyarbari Reuben',
author_email='anyaribari@gmail.com',
license='unlicense',
packages=['biotext'],
install_requires=['spacy','pandas'],
zip_safe= False
)
