#!/bin/bash
#
# clever_CONTROL.SH - run as a crontab job to create and sftp clever data files to naviance, jmix ESL class and SSO apps for students
#
# 
#
cd <<ENTER THE PATH TO THIS SCRIPT AND PYTHON FILES HERE>>/clever #go to absolute path of script
python3 clever_students.py  #create the students.csv
python3 staffAPI.py #create the teachers.csv to include all dorm parents, coaches etc
python3 cleve_school_csv.py #create one column made up school id to match with others csv
python3 clever_academic_sections_teachers.py #create sections.csv
python3 clever_academic_enrollments.py #create  enrollments.csv
python3 cleve_sftp.py #send data
