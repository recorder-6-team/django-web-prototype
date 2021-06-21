# Recorder 6 Django web prototype

This repository contains the code for a prototype illustrating the potential to use Python and
Django to develop a web application replacement for Recorder 6.

**Do not use this prototype on a production databas.**

The prototype currently implements a very small section of Recorder 6 functionality, namely the
login form, plus a tree browser for locations and the ability to edit the names or other basic
fields of a location.

## Installation

At this point, as this is a prototype the installation requires some manual steps and configration.

### Prerequisites

* Any operating system capable of running Python can be used (Windows, Max or Linux).
* The installation assumes that you have an installation of Recorder 6 available either on the
machine you are installing onto, or on the network where the database connection has been tested
from this machine.

**Please create a copy of your Recorder 6 database in order to test this prototype.**

### Steps

1. Install Python on your machine using the latest version at https://www.python.org/downloads/.
2. Make a folder on your machine and grab yourself a copy of the files using the Download button at
   https://github.com/recorder-6-team/django-web-prototype. You can download and unzip the files
   into your folder, or use `git clone` if you are familiar with Git.
3. Start your Command Line (Windows) or Terminal (Mac/Linux) application and navigate to the root
   folder of your installation. You should be inside a folder containing a file `requirements.txt`.
4. Enter the following commands to first create a virtual environment to keep the prototype's
   installation packages in, then to install these required packages:
   ```
   python -m venv ~/.virtualenvs/recorderdev
   %HOMEPATH%\.virtualenvs\recorderdev\Scripts\activate.bat
   pip install -r requirements.txt
   ```
   Note, if the 2nd command doesn't work try replacing `%HOMEPATH%` with ~.
5. In your installation folder, find the file `local_settings.example.py` and copy it to
   `local_settings.py`. Edit it in a text editor. You will need to find and replace the following
   tokens as follows:
     * `#insert-key-here#` - this must be replaced with a unique secret for your installation to
       ensure it is secure. You can generate a secret using a tool built into Django using the
       following command:
       ```
       python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
       ```
     * `#Insert name of testing database#` - The name of the database you are connecting to. For
       production this would typically be `NBNData` but make sure you are using a copy for testing
       the prototype.
     * `#insert datatabase host here#` - The SQL Server instance name you are connecting to. The
       correct setting for this can be obtained from Recorder 6's registry setting at `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Dorset Software\Recorder 6`
       under the key called `Server Name`.
     * `#Insert your name or your organisation name here#` - just set this to the name or your
       organisation would like to be indentified as.
     * `#Insert your 8 character recorder licence site ID here#` - your installation Site ID. For
       testing only, this can be set to `TESTDATA`.
   Now save the file. Note - if you are connecting from a non-Windows machine you will need to
   alter the database configuration in the settings file appropriately. More information is
   available at https://github.com/microsoft/mssql-django.
6. Because the package crispy-bootstrap5 has bugfixes in the latest code, which are not in the last
   set of released code  we need to uninstall crispy-bootstrap5 then reinstall using the version in
   Git.
   ```
   pip uninstall crispy-bootstrap5
   pip install git+git://github.com/django-crispy-forms/crispy-bootstrap5
   ```
7. Django provides built in functionality for handling user login. In order to make the Recorder 6
   `USER` table compatible with this functionality, you need to run the contents of each script in
   the `sqlserver_scripts` folder against your test database copy, e.g. using SQL Management
   Studio.

# Running the application

Once installed, from your command line or terminal run the following. Make sure you have activated
the Python virtual environment first as described above.

```
python manage.py runserver
```

Note that this method of running Python and Django is not intended for production use but it allows
the prototype code to be run easily.

Once the command has started Django, you will see somthing like the following in your output:
```
Performing system checks...

System check identified no issues (0 silenced).
June 21, 2021 - 12:21:39
Django version 3.1.12, using settings 'recorder.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

You can access the prototype by copying http://127.0.0.1:8000/ into your browser address bar.




