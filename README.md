# Recorder 6 Django web prototype

This repository contains the code for a prototype illustrating the potential to use Python and
Django to develop a web application replacement for Recorder 6.

:warning: **Do not use this prototype on a production database. Please create a copy of your
Recorder 6 database to use for testing this prototype.**

The prototype currently implements a small section of Recorder 6 functionality, namely the login
form, plus a tree browser for viewing and editing locations and features. Django's built in admin
interface provides tools for browsing the raw data and editing the lists of terms in for the
various lookups (e.g. location feature types).

## Installation options

Currently, there are 3 possible approaches to installing the Recorder 6 web-based prototype. Note
that you are installing a web-server, not a Windows application, and as such the installation is
more complex than a typical desktop application as it is not possible to provide a single "install
kit". However the installation only needs to be performed once and it can then be shared by
multiple users across a network, or even across the internet. Furthermore upgrades only need to be
performed in one place since the application is accessed via a web browser.

The following options for installation are provided:

1. Installation on the Windows Subsystem for Linux with Ubuntu
2. Manual installation directly onto your machine
3. Installation using Vagrant

Installation on the Windows Subsystem for Linux with Ubuntu is the most efficient way to get up and
running.

## Installation on the Windows Subsystem for Linux with Ubuntu

### Prerequisites

* Windows 10 or 11 is required for the Windows Subsystem for Linux feature.
* The installation assumes that you have an installation of Recorder 6 available either on the
machine you are installing onto, or on the network where the database connection has been tested
from this machine.

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
Firewall so that it allows WSL to connect to SQL Server. See
https://stackoverflow.com/questions/66126604/connect-local-sql-server-from-wsl2-ubuntu for an
explanation. To make this change:

1. Press the Windows key and type "cmd".
2. Select "Run as administrator" for the Command Prompt application and click Yes on the User
   Account Control popup box.
3. Copy the following command (without the $ prefix) and paste it into the Command Prompt and press
   return to run it:
   ```bash
   $ netsh advfirewall firewall add rule name=WSL_SQL dir=in protocol=tcp action=allow localport=1433 remoteip=localsubnet profile=any
   ```

Now close the Windows Command Prompt.

Next, because you are connecting to SQL Server from one machine to another (even though one machine
is virtual) you need to configure SQL Server for network access as described at the following link:
[Configure SQL Server for network access](docs/configure-sqlserver-network).

Return to the Ubuntu command-line shell window. Here are the commands you will need to copy and
paste into the shell and run, one at a time, with explanations for what each does. Note that you do
not need to copy the $ at the start of each statement:

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

3. Now, follow the steps described in the following link to configure the connection from the
   Recorder 6 web application to SQL Server: [Run the setup script](docs/run-setup-script)

4. Once the setup script has been run with no errors, you can prepare the Django migrations:
   ```bash
   $ python manage.py migrate
   ```

You can now proceed to the section entitled "Running the application" below.

## Manual installation

At this point, as this is a prototype the installation requires some manual steps and configuration.
Although the installation isn't trivial, please note that the prototype only needs to be installed
on a single machine as the application can run from a web-browser anywhere on the network.

### Prerequisites

* Any operating system capable of running Python can be used (Windows, Max or Linux).
* The installation assumes that you have an installation of Recorder 6 available either on the
machine you are installing onto, or on the network where the database connection has been tested
from this machine.
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
3. You now need to grab a copy of the application files. If you have Git installed and are familiar
   with it then doing a `git clone` is the preferred approach, but if not it is fine to download
   and unzip the files manually. So, either:
   * Start a command-line prompt then use Git - first using `cd` to navigate to a suitable folder in
     which to keep the application files:
     ```bash
      $ cd <a suitable folder>
      $ git clone https://github.com/recorder-6-team/django-web-prototype.git rec6
      $ cd rec6
      ```
   * Or, visit https://github.com/recorder-6-team/django-web-prototype then click the Code button
     then click Download ZIP. Unzip the folder into a suitable location on your hard-disk. Now
     press the Windows key, type "cmd" and click on the Command Prompt application to start it.
     Type the following to navigate into the folder where you unzipped the files (replacing
     <installation folder> with the path to the folder):
     ```bash
     $ cd "<installation folder>"
     ```
   You should now be inside a folder containing a file `requirements.txt` and a few other files
   and folders which you can confirm by typing the following to list the directory contents:
   ```bash
   $ dir
   ```

4. Rather than install packages required by the prototype globally, we'll create a virtual
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
5. Now, follow the steps described in the following link to configure the connection from the
   Recorder 6 web application to SQL Server:
   [Run the setup script](docs/run-setup-script)
6. Finally, run the following from your command-prompt/terminal in order to prepare the database:
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

This approach to installation of the Recorder web prototype uses a virtual machine to act as the
web-server, which saves installation of some of the required libraries in your Windows environment.
It will result in a self-contained installation of Linux Ubuntu with the Recorder web application
within it. Vagrant is a utility for managing virtual machines from the command-line which our setup
procedures make use of.

1. Because you are connecting to SQL Server from one machine to another (even though one machine is
   virtual) you need to configure SQL Server for network access as described at the following link:
   [Configure SQL Server for network access](docs/configure-sqlserver-network).

2. Install Vagrant using the appropriate package for your operating system from
   https://developer.hashicorp.com/vagrant/downloads. I installed Windows -> i686 as I am running
   an Intel Windows laptop. During the installation, accept the default options.

3. To install VirtualBox, which acts as a host for the virtual machine running Recorder 6, see
  [VirtualBox installation notes](docs/install-virtual-box).

4. You now need to grab a copy of the application files. If you have Git installed and are familiar
   with it then doing a `git clone` is the preferred approach, but if not it is fine to download
   and unzip the files manually. So, either:
   * Start a command-line prompt then use Git - first using `cd` to navigate to a suitable folder in
      which to keep the application files:
      ```bash
      $ cd <a suitable folder>
      $ git clone https://github.com/recorder-6-team/django-web-prototype.git rec6
      $ cd rec6
      ```
   * Or, visit https://github.com/recorder-6-team/django-web-prototype then click the Code button
      then click Download ZIP. Unzip the folder into a suitable location on your hard-disk. Now
      press the Windows key, type "cmd" and click on the Command Prompt application to start it.
      Type the following to navigate into the folder where you unzipped the files (replacing
      <installation folder> with the path to the folder):
      ```bash
      $ cd "<installation folder>"
      ```
   You should now be inside a folder containing a file `requirements.txt` and a few other files
   and folders which you can confirm by typing the following to list the directory contents:
   ```bash
   $ dir
   ```

3. Move `host_vars/default.example.yml` to `host_vars/default.yml` then edit in a text editor and
   configure appropriately.
4. Run the following:
   ```bash
   $ vagrant up
   ```
5. Browse to http://localhost:8000/.
