from setuptools import setup, find_packages 

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processimagedrm",
    version="0.0.1",
    author="Mayra",
    author_email="maymicabral@icloud.com",
    description="Process Images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maymicabral/pacote-processamento-imagem.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',

)