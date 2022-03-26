import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Andromeda',
    version='0.0.1',
    author='Oren Musicant',
    author_email='musicant.oren@gmail.com',

    description='Handy functions to handle simulation and physiological data',
    url=''https://github.com/ArielMobileLab/Andromeda',
    license='MIT',
    packages=['Andromeda'],
    install_requires=['numpy'],
