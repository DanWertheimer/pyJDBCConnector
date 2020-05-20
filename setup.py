import setuptools
from pyjdbcconnector import __version__

setuptools.setup(
    name='pyjdbcconnector',
    version=__version__,
    description='A high level JDBC API',
    url='https://github.com/DanWertheimer/pyJDBCConnector',
    download_url='https://github.com/DanWertheimer/pyJDBCConnector/archive/v0.1.5-alpha.tar.gz',
    author='Daniel Wertheimer',
    author_email='danwertheimer@gmail.com',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'JPype1 == 0.6.3',
        'JayDeBeApi >= 1.1.1',
        'PyHive == 0.6.2'

    ]
)
