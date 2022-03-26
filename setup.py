from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Andromeda',
    url='https://github.com/ArielMobileLab/Andromeda.git',
    author='Oren Musicant',
    author_email='musicant.oren@gmail.com',
    # Needed to actually package something
    packages=['Andromeda'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Handy function to handle simulation and physiological data',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
    download_url='https://github.com/ArielMobileLab/Andromeda.git'
)
