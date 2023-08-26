from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This fuction will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as fp:
        requirements=fp.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Divy Solanki',
    author_email='divysolanki7@gmail.com',
    packages=find_packages(),
    description='A machine learning project template for Python projects.',
    install_requires=get_requirements('requirements.txt')
)