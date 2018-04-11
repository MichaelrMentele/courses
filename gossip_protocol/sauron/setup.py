import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='sauron',
    version='1.0.0',
    url='',
    license='BSD',
    maintainer='michaelrmentele',
    maintainer_email='',
    description='T',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
