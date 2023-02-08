############################
#  to  create teachers.cv for CrisisGo Import
#  will pull all dorm parents=4343, advisors=4337, teachers=15,
#  coaches=18 and activity leaders=4623

from BbApiConnector import BbApiConnector
from bottle import request, response, post, get, put, delete
import json
import csv
import pandas as pd
import itertools
import sys
 ############### API Call #####################

api_conn = BbApiConnector('<<ADD PATH TO YOUR SECRETS HERE>>>>')
bb_session = api_conn.get_session()

#This will be a dictionary array to traverse each team id
#get teams into list/dictionary
roles_uri = f'https://api.sky.blackbaud.com/school/v1/users/extended?base_role_ids=15,4343,4337,18,4623'
req = bb_session.get(roles_uri)
staffResponse = json.loads(req.text)

############### iterate #####################

#interates through nested list to create a new nested list for output to csv
tempList = []
key_list =  ['first_name', 'last_name','id']
total = 0
for key,val in sorted(staffResponse.items()):
	if isinstance(val, list): # if dictionary contains a list
		for each_item in val: #for each item in list value
				for k,v in each_item.items(): # for each dictionary in list
					temp = str(v)

					if k in key_list:
						if k == 'first_name':
							k1 = k
							temp1 = temp
						elif k == 'last_name':
							k2 = k
							temp2 = temp
						elif k == 'id':
							k3 = k
							temp3 = temp
				k4 = "School_id"
				tempList.append({k1:temp1, k2:temp2, k3:temp3,k4:'HAHI'})
				total+=1
        
############### create CSV #####################
teachers_csv_headers=['First_name', 'Last_name', 'Teacher_id', 'School_id']

#uses pandas library to write to csv
df = pd.DataFrame(tempList)
df.drop_duplicates(subset=['id'],keep='first', inplace=True)
df.to_csv('teachers.csv', mode='w', index=False, header=teachers_csv_headers)

print('Total facstaff are: ',total)
