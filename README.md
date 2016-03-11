# BaseTest
Made for personal purpose!

#Usage

To run test suite:

.. code:: bash

    $ python setup.py install

#Windows platform
While running on Windows there could be a problem with setuptools library - env variables and windows register are not set properly.
Instead of changing path it's recommend to manually remove old library and install it using script. Steps to follow from command shell:

1) Remove existing libraries -->> 'pip uninstall setuptools'
2) Download script from website -->> 'powershell -Command "(New-Object Net.WebClient).DownloadFile('https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py', 'ez_setup.py')"'
3) Install packages -->> 'python ez_setup.py'


It could be automated using python script, python builder on Jenkins or exetute shell on Jenkins in following steps:

TRY:
    Import setuptools library
IF exception thrown, THAN
    Make reinstall libraries procedure