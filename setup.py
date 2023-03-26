from setuptools import setup,find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as f_obj:
        requirements=f_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name='Ml_project',
    version='0.01',
    author="Vishal Roy",
    author_email='vroy02243@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)