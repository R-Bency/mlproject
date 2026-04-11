from setuptools import find_packages,setup
from typing import List

noise='-e .'
def get_req(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as  file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if noise in requirements:
            requirements.remove(noise)

    return requirements

setup(
    name='fullmlproject',
    version='0.0.1',
    author='Bency',
    author_email='bennyedu11@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')

)