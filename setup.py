from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    # this function is going to return the requiement packages
    
    requirements=[]
    with open(file_path) as f:
        requirements=f.readline()
        requirements=[req.replace("\n","") for req in requirements]

        if "-e. " in requirements:
            requirements.remove("-e .")
    
    return requirements



setup(
    name="ML_PROJECT",
    version='0.0.1',
    author="Krushnakant",
    author_email="krushnaborude9007@gmail.com",
    packages=find_packages(),
    # install_requires=["Pandas","Numpy","Seaborn","Matplotlib"]  not feasible to write 100/1000 pakages
    install_requires=get_requirements("requirements.txt")

)
