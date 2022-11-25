# Configuring SQL Server for network access

One of the trickiest parts of this installation is persuading your virtual machine and your SQL
Server which holds your Recorder 6 data to communicate. In particular, although you may be running
the virtual machine containing the Recorder web application on the same machine as the SQL Server
database, because the virtual machine is in-effect a completely standalone machine (albeit virtual)
the system has to be configured to allow communication across the network. The default settings for
SQL Express will only allow communication with the database from the machine the database is
installed onto, so we have to change that limitation.

On the machine that the Recorder 6 database is running on (which will be your own machine if
running Recorder 6 standalone), click the Start menu, then type “Computer Management” and run the
application. Select Services and Applications > SQL Server Configuration Manager > SQL Server
Network Configuration > Protocols for <DBNAME> and make sure TCP/IP is enabled.

Also in the Computer Management application, click on SQL Server Services - ensure that SQL Service
Browser service is started; if not, right click on it and select “start”. If you want it to
automatically start on this machine after you restart your machine then right click on it and
select properties, then on the Service tab you can change the Start Mode to automatic.
