from setuptools import setup

setup(name='hypepy',
      version='0.1',
      description='A user-friendly and intuitive hypothesis testing package',
      url='https://github.com/UBC-MDS/hypepy',
      author='Ivan Despot, Siobhan McCarter, Joe Sastrillo',
      packages=['hypepy'],
      install_requires=[
          'numpy>=1.12',
          'pandas>=0.20'
      ],
      zip_safe=False)
