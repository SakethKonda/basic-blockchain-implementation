from hashlib import sha256
import json
import time
import csv

difficulty = 2

arrow = ' '*30+'|\n'+' '*30+'|\n'+' '*30 + 'v'

def print_block(data):
	print('-'*60)
	for k,v in data.items():
		print(f'|{k:<15} : {str(v):<40}|')
	print('-'*60)


sample_data = {
		'name': 'Sample Data', 
		'dob': 'DD-MM-YYYY', 
		'uidx': 'XXXX', 
		'acad_yr': 'YYYY-YY', 
		'course_start': 'DD-MM-YYYY', 
		'course_end': 'DD-MM-YYYY', 
		'subject': 'Subject Name', 
		'subject_code': 'Subject Code', 
		'marks': 'Marks obtained', 
		'remarks': 'Any additional comments or remarks', 
		'inst_name': 'Institute Name', 
		'inst_code': 'Institute Code', 
		'fac_code': 'Faculty Code',
		 'standard': 'Student standard'
 }