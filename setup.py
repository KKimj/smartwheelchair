import setuptools


install_requires = [
    'USBSerial>=1.0.1',
    'HC_SR04>=0.3.1',
]

try:
    # $ pip install pypandoc
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setuptools.setup (
    name = 'smartwheelchair',
    version = '0.0.1',
    license = 'GPL-3.0 License',
    description = 'smartwheelchair Python library',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author = 'KKimj',
    author_email = 'kkimj@hanyang.ac.kr',
    url = 'https://github.com/KKimj/smartwheelchair',

    install_requires=install_requires,

    py_modules=[""],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers = [
        # https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: Korean",
    ],
    python_requires='>=3',
)
