from BbApiConnector import BbApiConnector
from bottle import request, response, post, get, put, delete
import json
import csv
import pandas as pd
#import itertools
#import sys
import datetime
print("starting connection for enrollement.csv") 
  ############### API Call #####################
#api_conn = BbApiConnector('resources/app_secrets.json')
api_conn = BbApiConnector('/home/hpaadmin/BbApiConnector-Python/resources/app_secrets.json')
bb_session = api_conn.get_session()

#US = 1995, MS=1994  , LS=1993, summer=1996

ls_uri = f'https://api.sky.blackbaud.com/school/v1/academics/sections?level_num=1993'
req = bb_session.get(ls_uri)
responseOfLSSections = json.loads(req.text)

ms_uri = f'https://api.sky.blackbaud.com/school/v1/academics/sections?level_num=1994'
req = bb_session.get(ms_uri)
responseOfMSSections = json.loads(req.text)

us_uri = f'https://api.sky.blackbaud.com/school/v1/academics/sections?level_num=1995'
req = bb_session.get(us_uri)
responseOfUSSections = json.loads(req.text)


############### iterate LS #####################
ls_sections = []
count = 0
for key,value in responseOfLSSections.items():
	if isinstance(value, list): # if dictionary contains a list
		for each_item in value: #for each item in list value
			for k,v in each_item.items(): # for each dictionary in list
				temp = str(v)
				if k == 'name' and count <= 5:
					if 'HOMEROOM' in temp :
						section_id = each_item["id"]
						ls_sections.append(section_id)
						count+=1

print('LS enrollment iterate  Completed', count)

############ Iterate through list/dictionary of section to create roster ############
#For each section print out roster#
enrollment=[]
count=0
for v in ls_sections: #for each value in the list sections
	#for key, value in v.items():
		temp = str(v)
		enrollment_uri = f'https://api.sky.blackbaud.com/school/v1/academics/sections/{temp}/students'
		req = bb_session.get(enrollment_uri, params=temp)
		responseOfEnrollment = json.loads(req.text)
		count +=1
		for k,v in responseOfEnrollment.items():
				if not isinstance(v, int):
					for each in v:
						enrollment.append({"Student_id": each["id"], "Section_id": temp, "School_id":'LS1949'})
#print('iterate enrollment of each section Completed')

############### iterate MS #####################
ms_sections = []
count = 0
for key,value in responseOfMSSections.items():
	if isinstance(value, list): # if dictionary contains a list
		for each_item in value: #for each item in list value
				temp = str(v)
				if  len(each_item["teachers"]):
					section_id = each_item["id"]
					ms_sections.append(section_id)
					count =+1

print('MS enrollment iterate  Completed', count)

#### remove duplicate sections######
#result=[]
#count = 0
#for v in ms_sections: #for each value in the sections list 
#	for key, value in v.items():
#		if value not in result:
#			result.append(value)
#			count =+1

############ Iterate through list/dictionary of section to create roster ############
#For each section print out roster#

count=0
for v in ms_sections: #for each value in the list sections
	#for key, value in v.items():
		temp = str(v)
		enrollment_uri = f'https://api.sky.blackbaud.com/school/v1/academics/sections/{temp}/students'
		#print(enrollment_uri)m                     
		req = bb_session.get(enrollment_uri, params=temp)
		responseOfEnrollment = json.loads(req.text)
		count +=1
		for k,v in responseOfEnrollment.items():
				if not isinstance(v, int):
					for each in v:
						enrollment.append({"Student_id": each["id"], "Section_id": temp, "School_id":'MS1949'})
#print('iterate enrollment of each section Completed')


############### iterate US #####################
us_sections = []
key_list=['name','teachers', 'id' ]
count = 0
for key,value in responseOfUSSections.items():
	if isinstance(value, list): # if dictionary contains a list
		for each_item in value: #for each item in list value
			#for k,v in each_item.items(): # for each dictionary in list
				temp = str(v)
				#print (each_item)
				if  len(each_item["teachers"]):
					section_id = each_item["id"]
				us_sections.append(section_id)
				count =+1

print('US enrollment iterate  Completed', count)

#### remove duplicate sections######
#result=[]
#count = 0
#for v in us_sections: #for each value in the sections list 
#	for key, value in v.items():
#		if value not in result:
#			result.append(value)
#			count =+1

############ Iterate through list/dictionary of section to create roster ############
#For each section print out roster#

count=0
for v in us_sections: #for each value in the list sections
	#for key, value in v.items():
		temp = str(v)
		enrollment_uri = f'https://api.sky.blackbaud.com/school/v1/academics/sections/{temp}/students'
		#print(enrollment_uri)m                     
		req = bb_session.get(enrollment_uri, params=temp)
		responseOfEnrollment = json.loads(req.text)
		count +=1
		for k,v in responseOfEnrollment.items():
				if not isinstance(v, int):
					for each in v:
						temp=int(temp)
						enrollment.append({"Student_id": each["id"], "Section_id": temp, "School_id":'US1949'})
#print('iterate enrollment of each section Completed')


#### remove duplicate sections######
#result=[]
#count = 0
#for v in sections: #for each value in the sections list 
#	for key, value in v.items():
#		if value not in result:
#			result.append(value)
#			count =+1


############### create CSV #####################
#schools_csv_headers=['School_id','School_name']
#teachers_csv_headers=['School_id','Teacher_id', 'First_name', 'Last_name']
#students_csv_headers=['School_id', 'Student_id', 'Last_name', 'First_name']
#sections_csv_headers = ['Name','Teacher_id', 'Section_id','School_id', 'Term_start', 'Term_end']
enrollments_csv_headers=['Student_id', 'Section_id', 'School_id']
#df_clean = df.drop_duplicates(subset=['timestamp', 'user_id'])
print("Creating enrollment.csv")
#uses pandas library to write to csv
df = pd.DataFrame(enrollment)
#df=df.drop_duplicates(subset=['Section_id','Student_id'], inplace=True, keep='first')

#remove Section example: uncomment to use
#df = df[df['Section_id'] != 24358738]
#df = df[df['Section_id'] != 24358740]
#df = df[df['Section_id'] != 24359404]
#df = df[df['Section_id'] != 24359406]
#df = df[df['Section_id'] != 24359226]
#df = df[df['Section_id'] != 24359228]
#df = df[df['Section_id'] != 24358744]
#df = df[df['Section_id'] != 24358746]

df.to_csv('enrollments.csv', mode='w',index=False, header=enrollments_csv_headers)

print ('enrollment.csv complete', count)
#df_clean = df.drop_duplicates(subset=['Section_id'],keep='first',inplace=True)

#print (df_clean)
#df_state=pd.read_csv("sections.csv")
