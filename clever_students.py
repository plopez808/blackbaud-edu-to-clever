############################
#  to  create teachers.cv for CrisisGo Import
#  will pull all students=14.

from BbApiConnector import BbApiConnector
from bottle import request, response, post, get, put, delete
import json
import csv
import pandas as pd
import itertools
import sys
from datetime import datetime

print("Starting students.csv")
 ############### API Call #####################

api_conn = BbApiConnector('<<INSERT YOUR PATH TO SECRETS HERE')
bb_session = api_conn.get_session()
print("connected for student download")
#get grad year for iterating through student school levels
current_year = datetime.today().year
current_month = datetime.today().month

if current_month >= 8:
	grad_year = current_year + 1
else:
	grad_year = current_year

current_senior_year = grad_year

#This will be a dictionary array to traverse each student id by role
#get student role 14 into list/dictionary
#roles_uri = f'https://api.sky.blackbaud.com/school/v1/users/extended?base_role_ids=14'
##iterate through grad years current year -1 until kindergarten
grad_year_count = 1

while grad_year_count <= 13:
	roles_uri = f'https://api.sky.blackbaud.com/school/v1/users/extended?base_role_ids=14&grad_year={grad_year}'
	#print(roles_uri)
	grad_year_count += 1
	grad_year += 1
	req = bb_session.get(roles_uri)
	studentResponse = json.loads(req.text)

	############### iterate #####################

	#interates through nested list to create a new nested list for output to csv
tempList = []
key_list =  ['first_name', 'last_name','id', 'email', 'grad_year','birth_date', 'student_info']
for key,val in sorted(studentResponse.items()):
	if isinstance(val, list): # if dictionary contains a list
		for each_item in val: #for each item in list value
			for k,v in each_item.items(): # for each dictionary in list
				temp = str(v)
				if k in key_list:
					if k == 'first_name':
						k1 = k
						temp1 = temp
						#print("k1:",k1, "temp1:",temp1)
					elif k == 'last_name':
						k2 = k
						temp2 = temp
						#print("k2:",k2, "temp:",temp2)
					elif k == 'id':
						k3 = k
						temp3 = temp
						#print("k3:",k3, "temp:",temp3)
					elif k == 'email':
						k4 = k
						temp4 = temp
						#print("k4:",k4, "temp:",temp4)
					elif k == 'birth_date':
						k8 = "DOB"
						temp = temp[:10]
						temp = datetime.strptime(temp,'%Y-%m-%d')
						temp8 = datetime.strftime(temp,"%m/%d/%Y")
						#print("k8:",k8, "temp:",temp8)
					elif k == "student_info":

						k5 = "grad_year"
						temp5 = int(each_item["student_info"]["grad_year"])
						k6 ="grade_level_abbreviation"
						temp=each_item["student_info"]["grade_level_abbreviation"]
						if temp == "K":
							temp6 = 'Kindergarten'
						elif temp == "PG":
							temp6 = 'PostGraduate'
						else:
							temp6 = each_item["student_info"]["grade_level_abbreviation"]
					k7 = "School_id"
			if temp5 <=(current_senior_year + 4): #if student grad year is greather than or equal to 2025
				tempList.append({k1:temp1, k2:temp2, k3:temp3,k4:temp4,k8:temp8,k5:temp5,k6:temp6,k7:'US1949'})

				#if student grad year is greather than or == to 2026 AND grad year is less than or = 2028
			elif temp5 >= (current_senior_year + 5)	and temp5 <=(current_senior_year + 7):
				tempList.append({k1:temp1, k2:temp2, k3:temp3,k4:temp4,k8:temp8,k5:temp5,k6:temp6, k7:'MS1949'})

				#if student grad year is greather than or == to 2029 AND grad year is less than or = 2035
			elif temp5 >=(current_senior_year + 8)	and temp5 <=(current_senior_year + 13):
				tempList.append({k1:temp1, k2:temp2, k3:temp3,k4:temp4,k8:temp8,k5:temp5,k6:temp6,k7:'LS1949'})

############### create CSV #####################
students_csv_headers=[ 'First_name', 'Last_name', 'Student_id','Student_email', 'DOB', 'Graduation year', 'Grade', 'School_id'  ]

print("creating students.csv")
#uses pandas library to write to csv

df = pd.DataFrame(tempList)
df.to_csv('students.csv',index=False, header=students_csv_headers)
print ('student csv complete')
