from setuptools import find_packages, setup

setup(
    name='UROP'
    version='0.1.0'
    packages=find_packages(),
    install_requires=[
        'PyQt5'
        'pymongo'
    ],
    entry_points={
        'console_scripts':[
            'project=my_module.main:main_function', # Edit this later
        ],
    },
    python_requires='>=3.6',
    author='Elva Chen Yiyang',
    author_email='elvachen2000@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/orz9/UROP',
)