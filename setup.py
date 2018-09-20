import setuptools
from cakedoctor.version import Version


setuptools.setup(name='cakedoctor',
                 version=Version('1.0.0').number,
                 description='Python Package for CakeDoctor',
                 long_description=open('README.md').read().strip(),
                 author='Swat Team',
                 author_email='swat-team@sysco.com',
                 url='https://wiki.leapset.com/pages/viewpage.action?pageId=93128187',
                 py_modules=['cakedoctor'],
                 install_requires=[],
                 license='Sysco License',
                 zip_safe=False,
                 keywords='cakedoctor package',
                 classifiers=['Packages', 'Boilerplate'])
