# Script to configure this installation.
# Copies the example local settings py file and populates the placeholders from user input.

from django.core.management import utils
import sys

while True:
  database = input('Enter the Recorder database name (press Enter for default value NBNData): ').strip() or 'NBNData'
  if database == '':
    print('A value for the Recorder database name is required')
  else:
    break

while True:
  host = input('Enter the Recorder database host name (please see installation documentation): ').strip()
  if host == '':
    print('A value for the Recorder database host is required')
  else:
    break

while True:
  user = input('Enter the Recorder database user name (press Enter for default value NBNUser): ').strip() or 'NBNUser'
  if user == '':
    print('A value for the Recorder database host is required')
  else:
    break

while True:
  password = input('Enter the Recorder database user password (press Enter for default value NBNPassword): ').strip() or 'NBNPassword'
  if password == '':
    print('A value for the Recorder database user password is required')
  else:
    break

while True:
  organisation = input('Enter the name of the organisation or person responsible for this installation: ').strip()
  if organisation == '':
    print('A value for the organisation is required')
  else:
    break

while True:
  siteId = input('Enter the 8 character site ID for this installation: ').strip()
  if siteId == '':
    print('A value for the site ID is required')
  elif len(siteId) != 8:
    print('The site ID must be 8 characters long')
  else:
    break

# Read in the file
with open('recorder/local_settings.example.py', 'r') as file:
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('{{ recorder_secret_key }}', utils.get_random_secret_key())
filedata = filedata.replace('{{ recorder_database_name }}', database)
filedata = filedata.replace('{{ recorder_database_host }}', host)
filedata = filedata.replace('{{ recorder_database_user }}', user)
filedata = filedata.replace('{{ recorder_database_password }}', password)
filedata = filedata.replace('{{ recorder_organisation_name }}', organisation)
filedata = filedata.replace('{{ recorder_site_id }}', siteId)

# Now test the connection.
from recorder.local_settings import DATABASES
import pyodbc

try:
  cnxnStr = ("Driver=" + DATABASES['default']['OPTIONS']['driver'] + ";"
              "Server=" + DATABASES['default']['HOST'] + ";"
              "Database=" + DATABASES['default']['NAME'] + ";"
              "UID=" + DATABASES['default']['USER'] + ";"
              "PWD=" + DATABASES['default']['PASSWORD'] + ";")
  cnxn = pyodbc.connect(cnxnStr)
except Exception as error:
  print('The connection to SQL Server failed. Please review the settings in recorder/local_settings.py or run setup.py again.')
  print('The error message was: ' + repr(error))
  sys.exit("Configuration failed and the local settings file has not been created.")

# Create the local settings file with the user input parameter values added.
with open('recorder/local_settings.py', 'w') as file:
  file.write(filedata)

# Run the user table update script - it is safe to re-run multiple times.
cursor = cnxn.cursor()
with open('sqlserver_scripts/USER.sql', 'r') as file:
  sql = file.read()

queries = sql.split('\nGO')
for query in queries:
  cursor.execute(query)

print('A column called Django_USERNAME has been added to the USER table, allowing the web based login form to work.')
print('')
print('## Configuration complete. Run the application using the following command (substitute python for python3 if necessary). ##')
print('python manage.py runserver')

