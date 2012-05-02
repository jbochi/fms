from setuptools import setup, find_packages

README = open('README.md').read()

setup(name='fms',
      version='0.0.1',
      description='FMS API client',
      long_description=README,
      author='Juarez Bochi',
      author_email='jbochi@gmail.com',
      packages=['fms'],
      include_package_data=True,
      install_requires=['requests==0.11.2'],
      tests_require=[],
      )