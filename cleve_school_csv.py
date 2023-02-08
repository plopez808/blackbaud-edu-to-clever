#######################
# REMOVE ANY SECTIONS YOU DO NOT NEED

import csv
import pandas as pd

print("creating schools.csv")
############### create CSV #####################
schools_csv_headers=['School_id','School_name','School_number','School_address','School_city','School_zip' ]

data= {
	'School_id':['US1949'],
	'School_name':['Upper School'],
        'School_number':['US1949'],
        'School_address':['<<<ENTER YOUR ADDRESS HERE>>>'],
        'School_city':['<<<ENTER YOUR CITY HERE>>>'],
        'School_zip':['<<<ENTER YOUR ZIP HERE>>>']

}
df =pd.DataFrame(data)
df.to_csv('schools.csv', mode='w',index=False, header=schools_csv_headers)
data= {
        'School_id':['MS1949'],
        'School_name':['Middle School'],
        'School_number':['MS1949'],
        'School_address':['<<<ENTER YOUR ADDRESS HERE>>>'],
        'School_city':['<<<ENTER YOUR CITY HERE>>>'],
        'School_zip':['<<<ENTER YOUR ZIP HERE>>>']

}
df =pd.DataFrame(data)
df.to_csv('schools.csv', mode='a',index=False)
data= {
        'School_id':['LS1949'],
        'School_name':['Lower School'],
        'School_number':['LS1949'],
        'School_address':['<<<ENTER YOUR ADDRESS HERE>>>'],
        'School_city':['<<<ENTER YOUR CITY HERE>>>'],
        'School_zip':['<<<ENTER YOUR ZIP HERE>>>']

}
#schools_csv_headers=['School_id','School_name','School_number','School_address','School_city','School_zip' ]
df =pd.DataFrame(data)
df.to_csv('schools.csv', mode='a',index=False)
print('school.csv created')
