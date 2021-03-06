from setuptools import setup, find_packages


setup(
    name='pycldf',
    version='1.14.2.dev0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='A python library to read and write CLDF datasets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='',
    license='Apache 2.0',
    url='https://github.com/cldf/pycldf',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'cldf=pycldf.__main__:main',
        ],
    },
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'csvw>=1.7',
        'clldutils>=3.5',
        'uritemplate>=3.0',
        'python-dateutil',
        'pybtex',
    ],
    extras_require={
        'catalogs': [
            'cldfcatalog',
            'pyglottolog',
            'pyconcepticon',
        ],
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'cldfcatalog',
            'pyglottolog',
            'pyconcepticon',
            'mock',
            'pytest>=4.3',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
