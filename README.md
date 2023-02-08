# Blackbaud Education Management APIs to FTP Clever 
You will need BbApiConnector-Python found here in Github. 
Go will need access to Blackbaud K-12 Developer Sky API subscription. 
You will need to create an Blackbaud App for the API to run.
In the BbApi Connector resources => app_secrets JSON file add the app id from the app you created, app secret, tokens you get from the setup up the BbApi Connector, subscription key from the app you created, and the URI which is localhost:port/callback. 
You will need to intall the panda, requests, pysftp, jsonify BbApiConnector-justein python library. 

Add clever_control.sh to cronjobs to run nightly or however often you choose. 
The script clever_control.sh runs the following python scripts via a nightly cronjob.

clever_students.py #grabs all students and creates students.csv
clever_academic_sections_teachers.py #grabs teachers and their sections and creates teachers.csv and sections.csv
cleve_school_csv.py #creates generic schools file. school_id can be anything we choose and creates schools.csv
but has to match in the other files
clever_academic_enrollment.py #creates academic sections with students enrolled and creates enrollments.csv

to produce the following
schools.csv #per crisisgo Documentation bldg name must match school name
students.csv #no duplicate student ids
teachers.csv #no duplicate teacher ids 
sections.csv #no duplicate section ids teachers must exist in previous csv
enrollments.csv #student ids and section ids must exist in previous csv

and then runs
cleve_sftp.py 
to send all 5 csvs via sftp to Clever. 
There is a nightly autosyn in Clever portal. 
This can also be manually completed for testing.

