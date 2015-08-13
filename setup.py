from setuptools import setup

setup(
    name='DataStructuresSerialized',
    version='0.0.2',

    description='python data structures(tuple list OrderedDict) serialized',
    long_description=open('README.rst').read(),
    url='https://github.com/laodifang/DataStructuresSerialized',
    author='Ren Peng',
    author_email='ithink.ren@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='data structures list serialized deserialization',

    packages=['tests'],
    py_modules=['DataStructuresSerialized'],
    test_suite='tests',
)
