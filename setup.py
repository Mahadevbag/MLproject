from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements from the given file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # remove newline characters
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # remove '-e .' if present
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Mahadev Bag',
    author_email='bagmahadev1010@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
