# Recorder 6 Django web prototype

This repository contains the code for a prototype illustrating the potential to use Python and
Django to develop a web application replacement for Recorder 6.

**Do not use this prototype on a production database.**

The prototype currently implements a very small section of Recorder 6 functionality, namely the
login form, plus a tree browser for viewing and editing locations and features.

## Installation options

Currently, there are 3 possible approaches to installing the Recorder 6 web-based prototype. Note
that you are installing a web-server, not a Windows application, and as such the installation is
more complex than a typical desktop application. However the installation only needs to be
performed once and it can then be shared by multiple users across a network, or even across the
internet. Furthermore upgrades only need to be performed in one place since the application is
accessed via a web browser.

Three options for installation are provided:

1. Installation on the Windows Subsystem for Linux with Ubuntu
2. Manual installation directly onto your machine
3. Installation using Vagrant

Installation on the Windows Subsystem for Linux with Ubuntu is the most efficient way to get up and
running,

## Installation on the Windows Subsystem for Linux with Ubuntu

### Prerequisites

* Windows 10 or 11 is required for the Windows Subsystem for Linux feature.
* The installation assumes that you have an installation of Recorder 6 available either on the
machine you are installing onto, or on the network where the database connection has been tested
from this machine.

**Please create a copy of your Recorder 6 database in order to test this prototype.**

### Steps

Windows 10 and later have a feature called Windows Subsystem for Linux (WSL) which allows the Linux
operating system environment to run as an application inside Windows. We can run the Recorder 6 web
application on WSL which avoids the need to install some large components required to run certain
Django modules on Windows, which are not required when running on Linux. Although you do need to
install a couple of applications and run some setup commands, the actual steps required should
individually be fairly simple.

There is documentation on installation of WSL and Ubuntu at
https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview. Both
are available as Windows applications in the Microsoft Store. You do not need to perform the steps
under the section "Install and use a GUI package" since we only need the main server components,
not the Ubuntu desktop.

Once you get to the end of step 4 - Configure Ubuntu, you should have a command line "shell"
running for your Ubuntu environment. Before we go any further though, we need to modify the Windows
Firewall so that it allows WSL to connect to SQL Server. See https://stackoverflow.com/questions/66126604/connect-local-sql-server-from-wsl2-ubuntu
for an explanation. To make this change:

1. Press the Windows key and type "cmd".
2. Select "Run as administrator" for the Command Prompt application and click Yes on the User
   Account Control popup box.
3. Copy and paste the following command and run it (without the $ prefix):
   ```bash
   $ netsh advfirewall firewall add rule name=WSL_SQL dir=in protocol=tcp action=allow localport=1433 remoteip=localsubnet profile=any
   ```

Now close the Windows Command Prompt.

Next, because you are connecting to SQL Server from one machine to another (even though one machine
is virtual) you need to configure SQL Server for network access as described at the following link:
[Configure SQL Server for network access](docs/configure-sqlserver-network).

Return to the Ubuntu shell window. Here are the commands you will need to copy and paste into the
shell and run, one at a time, with explanations for what each does. Note that you do not need to
copy the $ at the start of each statement:

1. Get the latest Recorder 6 web application source code into a subfolder called `rec6`.
```bash
$ git clone https://github.com/recorder-6-team/django-web-prototype.git rec6
$ cd rec6
```

2. Set the permissions then run a script that installs various required installation packages:
```bash
$ chmod +x install-packages.sh
$ sudo ./install-packages.sh
$ git checkout install-packages.sh
```

Now, follow the steps described below to configure the connection from the Recorder 6 web
application to SQL Server:
[Run the setup script](docs/run-setup-script)

Once the setup script has been run with no errors, you can prepare the Django migrations:
```bash
$ python manage.py migrate
```

Then you should be ready to start the Recorder 6 application as follows:
```bash
$ python3 manage.py runserver
```

This will start the Python script which runs the Django web-server process. You should see
something similar to the following output in the shell when the application is ready:
```
Django version 4.0.7, using settings 'recorder.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The application can now be accessed at using a web browser at http://127.0.0.1:8000/.

## Manual installation

At this point, as this is a prototype the installation requires some manual steps and configuration.
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
6. Now, follow the steps described below to configure the connection from the Recorder 6 web
   application to SQL Server:
   [Run the setup script](docs/run-setup-script)
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

TODO - Update from Vagrant installation notes

To install VirtualBox, which acts as a host for the virtual machine running Recorder 6, see
[VirtualBox installation notes](docs/install-virtual-box).

1. Install vagrant
2. Install ansible
3. move `host_vars/default.example.yml` to `host_vars/default.yml` and configure appropriately
4. `$ vagrant up`
5. browse to http://localhost:8000/
