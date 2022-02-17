# Recorder 6 Django web prototype

This repository contains the code for a prototype illustrating the potential to use Python and
Django to develop a web application replacement for Recorder 6.

**Do not use this prototype on a production databas.**

The prototype currently implements a very small section of Recorder 6 functionality, namely the
login form, plus a tree browser for locations and the ability to edit the names or other basic
fields of a location.

## Installation

At this point, as this is a prototype the installation requires some manual steps and configration.
Although the installation isn't trivial, please note that the prototype only needs to be installed
on a single machine as the application can run from a web-browser anywhere on the network.

### Prerequisites

* Any operating system capable of running Python can be used (Windows, Max or Linux).
* The installation assumes that you have an installation of Recorder 6 available either on the
machine you are installing onto, or on the network where the database connection has been tested
from this machine.

**Please create a copy of your Recorder 6 database in order to test this prototype.**

### Steps

1. If using Windows, install Python on your machine using the latest version at
   https://www.python.org/downloads/ (currently version 3.9). During the installation, select the
   option to add Python to the PATH environment variable. At the end of the installation you will
   be asked if it is OK to remove the MAX_PATH limitation, please allow this.

   For other operating systems you should find it is already installed, but if not then please
   install it.

   Note that this installation has not been tested using the version of Python available via the
   Windows Store.
2. Also if running Windows, please install the Microsoft Visual C++ Build Tools from
   https://visualstudio.microsoft.com/visual-cpp-build-tools/. During the installation, select
   "Desktop development with Visual C++" from the Workloads tab.
3. Make a folder on your machine and grab yourself a copy of the files using the Download button at
   https://github.com/recorder-6-team/django-web-prototype. You can download and unzip the files
   into your folder, or use `git clone` if you are familiar with Git.
4. Start your Command Line application using Run as Administrator (Windows) or Terminal (Mac/Linux)
   application and navigate to the root folder of your installation by entering the following,
   replacing <path> with your installation path:
   ```
   cd <path>
   ```
   You should be inside a folder containing a file `requirements.txt` and a few other files and
   folders.
5. Rather than install packages required by the prototype globally, we'll create a virtual
   environment, which makes it easy to keep everything separate. There are some handy notes on this
   at https://python.land/virtual-environments/virtualenv.

   On Windows, enter the following commands to first create a virtual environment to keep the
   prototype's installation packages in, then to install these required packages. For other
   operating systems please refer to the notes in the above link for modifications:
   ```
   python -m venv %HOMEPATH%/.virtualenvs/recorderdev
   %HOMEPATH%\.virtualenvs\recorderdev\Scripts\activate.bat
   pip install -r requirements.txt
   ```
   Notes:
   * The second command above `%HOMEPATH%\.virtualenvs\recorderdev\Scripts\activate.bat` activates
     the recorderdev virtual environment. When you do this, your command-prompt should show
     (recorderdev) to the left of the commands you input - this indicates the command will run
     inside that virtual environment and any Python packages you install will be contained within
     the `recorderdev` environment. This helps ensure that different Python projects you are
     working on don't 'pollute' each other with different package versions and it also makes it
     easier to clean up everything to do with that project. _If you start a new command prompt or
     terminal, or you notice the (recorderdev) prefix has gone, just re-run this command to
     re-start the virtual environment.
   * If running Mac or Linux and you find any of the commands fail due to lack of permissions,
     re-run the command with `sudo ` added to the start of the command:
6. In your installation folder, find the file `recorder/local_settings.example.py` and copy it to
   `recorder/local_settings.py`. Edit it in a text editor. You will need to find and replace the following
   tokens as follows:
     * `#insert-key-here#` - this must be replaced with a unique secret for your installation to
       ensure it is secure. You can generate a secret using a tool built into Django using the
       Python shell by running the following commands from your command prompt. The first command
       starts the shell, then the >>> indicates that subsequent commands will run using the Python
       interpreter:
       ```
       python
       >>> from django.core.management import utils
       >>> print(utils.get_random_secret_key())
       >>> exit()
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

   Also, note that the database connection configuration given here requires Windows Authentication
   to be enabled. If you would prefer to connect as a named user, you can set the `USER`, `PASSWORD`
   and `Trusted_Connection=no` options as described at https://github.com/microsoft/mssql-django.
   The connection method you use must be for a user with rights to select and modify data in the
   `NAME`, `USER`, `LOCATION`, `LOCATION_NAME` and `LOCATION_TYPE` tables.
7. Django provides built in functionality for handling user login. In order to make the Recorder 6
   `USER` table compatible with this functionality, you need to run the contents of each script in
   the `sqlserver_scripts` folder against your test database copy, e.g. using SQL Management
   Studio.
8. Finally, run the following from your command-prompt/terminal in order to prepare the database:
   ```
   python manage.py migrate
   ```

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

# Installing and running through vagrant

1. Install vagrant
2. Install ansible
3. move `host_vars/default.example.yml` to `host_vars/default.yml` and configure appropriately
4. `$ vagrant up`
5. browse to http://localhost:8000/
