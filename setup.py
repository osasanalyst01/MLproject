from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [
            line.strip()
            for line in file_obj
            if line.strip() and not line.startswith("-e")
        ]
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Osasanalyst01",
    author_email="osasereokunloye@gmail.com",
    packages=find_packages(where="src"),   # <-- look inside src folder
    package_dir={"": "src"},               # <-- tells setuptools that packages live in src/
    install_requires=get_requirements("requirements.txt"),
)
