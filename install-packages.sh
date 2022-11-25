#Install a package required for ODBC database connections.
sudo apt install unixodbc-dev
#Install a Python package manager utility called pip.
sudo apt install python3-pip
#Get a key required for access to Microsoft's packages list.
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
#Now, add Microsoft's packages list to the package list available on this machine.
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
#See https://www.omgubuntu.co.uk/2017/08/fix-google-gpg-key-linux-repository-error.
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt-get update
#Install the tools required for accessing SQL Server.
sudo apt install mssql-tools
#Install the packages listed as requirements for the application.
pip install -r requirements.txt