#/usr/local/bin/python3
#
# sftp_test.py - sftp's a 5 test files to Clever server
#
#
#

import pysftp

host ='sftp.clever.com'
password ='<<<<<<ENTER YOUR SFTP PASSWORD HERE>>>>>>>'
username = '<<<<<<ENTER YOUR SFTP USERNAME HERE>>>>>>>'
log = '<<<<<<ENTER YOUR PATH TO WHERE YOU WANT YOUR LOG HERE>>>>>>>'

with pysftp.Connection(host, username=username, password=password, log=log) as sftp:
	sftp.put('<<PATH TO schools.csv>>>','<<clevers path to /home/your username/schools.csv')
	sftp.put('<<PATH TO teachers.csv>>>>','<<clevers path to /home/your username/steachers.csv')
	sftp.put('<<PATH TO students.csv>>>>>','<<clevers path to /home/your username/sstudents.csv')
	sftp.put('<<PATH TO sections.csv>>>>','<<clevers path to /home/your username/ssections.csv')
	sftp.put('/<<PATH TO enrollments.csv>>>>','<<clevers path to //home/your username/senrollments.csv')
	sftp.close()
print ('upload complete')
