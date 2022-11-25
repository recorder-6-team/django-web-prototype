# Running the setup.py script

Run a script that assists with the configuration required in order to connect to your SQL Server:
```bash
$ python3 setup.py
```

Or, if your python is installed as just "python":
```bash
$ python setup.py
```

This will guide you through the settings required by the application. The following settings are
requested:

* Recorder database name - this will normally be NBNData.

* Recorder database host name - this is the name of the SQL Server used in the connection.
  When connecting from a Windows machine to SQL Server, the host name is normally the name of the
  Windows machine, followed by a backslash, then the name of the SQL Server instance. So, something
  like MYMACHINE\SQLEXPRESS. To find out the host name your machine is using, press Windows-R,
  then enter regedit and click OK. Click Yes on the User Account Control dialog and it will start
  the Windows Registry Editor. Using the tree on the left, browse to
  Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Dorset Software\Recorder 6. The host name is the
  value given for the “Server Name”.

  However, when connecting from our Linux virtual machine, the SQL Server client code won't
  recognise the Windows machine name, so this needs to be replaced by the local IP address of the
  machine that the machine is running from, which gives a way of identifying the machine that can
  be recognised across different operating systems. From the command line, run:

  $ ipconfig | findstr /C:"IPv4 Address"

  This should output something like the following. The IP address we want is the one starting
  192.168.1. (the other one is used by my ethernet adaptor).
  ```bash
  C:\Windows\System32>ipconfig | findstr /C:"IPv4 Address"
   IPv4 Address. . . . . . . . . . . : 192.168.88.1
   IPv4 Address. . . . . . . . . . . : 192.168.1.138
   IPv4 Address. . . . . . . . . . . : 172.24.179.1
  ```

  So, to correctly set the recorder database host setting, use this IP address, followed by 2
  backslashes (not one!) and then the name of the SQL Server instance, which is probably SQLEXPRESS
  if you are using a default install of SQL Server Express.
* Recorder database user name - this needs to be a user account on the SQL Server which has read
  and write access to the database tables. The default is NBNUser.
* Recorder database password - the password for the above user. The default is NBNPassword.
* Organisation name - the name of the organisation which is hosting the network setup of Recorder 6
  and which will be displayed on the splash screen.
* Site ID - the installation's Site ID (8 character code).

Setup.py will also run a small script which adds a new column to the database USER table called
Django_username. This is required in order to allow the built in log-in processes in Django to
work. You can revert this change by deleting the `Django_username` column from the `USER` table.

If the connection to SQL Server fails, then an error will be reported. You can either run the
setup.py script again to alter the settings, or you can edit the recorder/local_settings.py file
directly using the `vi` editor. More information on the settings is available at
https://github.com/microsoft/mssql-django.

   Also, note that the database connection configuration given here requires Windows Authentication
   to be enabled. If you would prefer to connect as a named user, you can set the `USER`, `PASSWORD`
   and `Trusted_Connection=no` options as described at https://github.com/microsoft/mssql-django.
   The connection method you use must be for a user with rights to select and modify data in the
   following tables:
   * `NAME`
   * `USER`
   * `DAMAGE_OCCURRENCE`
   * `LOCATION`
   * `LOCATION_FEATURE`
   * `LOCATION_FEATURE_GRADING`
   * `LOCATION_FEATURE_TYPE`
   * `LOCATION_NAME`
   * `LOCATION_TYPE`
   * `POTENTIAL_THREAT`