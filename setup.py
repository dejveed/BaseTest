from setuptools import setup, find_packages

setup(
    name='BaseTest',
    version='1.0',
    description='Base sample lead flow test',
    author='Dawid Pacia',
    author_email='paciadawid@gmail.com',
    url='https://github.com/dejveed/BaseTest',
    packages=find_packages(),
    test_suite='tests',
    install_requires=['basecrm'],
    tests_require=['nose'],
    use_2to3=True,
    classifiers=[
        # Indicate who your project is intended for
        "Intended Audience :: Developers & Recruiters : ) ",
        "Topic :: Software Development",

        "Operating System :: OS Independent",

        #Supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ])