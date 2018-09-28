import setuptools
from monitor.version import Version


setuptools.setup(name='monitor',
                 version=Version('1.0.0').number,
                 description='Python Package for monitor device operations',
                 long_description=open('README.md').read().strip(),
                 author='Anandafit',
                 author_email='anandafit@gmail.com',
                 url='',
                 py_modules=['monitor'],
                 install_requires=[],
                 license='Sysco License',
                 zip_safe=False,
                 keywords='device monitor package',
                 classifiers=['Packages', 'Boilerplate'])
