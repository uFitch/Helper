from setuptools import setup, find_namespace_packages

setup(name='helper',
      version='1.0.5',
      description='Personal assistant-helper. Addressbook. Notebook. Folder cleaner',
      author='Andriy Onufriyenko',
      author_email='7206130@gmail.com',
      license='MIT',
      entry_points={'console_scripts': ['helper=helper.main:main']},
      include_package_data=True,
      packages=find_namespace_packages())
