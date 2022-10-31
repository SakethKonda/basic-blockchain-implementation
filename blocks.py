# Importing required modules
from util import *

class Block:
	'''
	Class which depicts each block of blockchain
	'''
	def __init__(self,index,details,timestamp,prev_hash):
		# Initialising the block
		self.index = index
		self.prev_hash = prev_hash
		self.nonce = 0
		self.timestamp = timestamp
		self.hash = None
		self.name = details['name']
		self.dob = details['dob']
		self.uidx = details['uidx']
		self.acad_yr = details['acad_yr']
		self.course_start = details['course_start']
		self.course_end = details['course_end']
		self.subject = details['subject']
		self.subject_code = details['subject_code']
		self.marks = details['marks']
		self.remarks = details['remarks']
		self.inst_name = details['inst_name']
		self.inst_code = details['inst_code']
		self.fac_code = details['fac_code']
		self.standard = details['standard']

	def compute_hash(self):
		# Function that returns hash of the block
		block_string = json.dumps(self.__dict__,sort_keys=True)
		return sha256(block_string.encode()).hexdigest()

	def return_details(self,auth=1):
		'''
		Used to return the block contains based on auth level
		auth level : Contents
		0 - Developer mode - Displays most of the contents
		1 - Admin mode -  Displays the student info including uidx, fac_code
		2 - Teacher mode - Displays only info related to education like subject, marks, institution
		'''
		details = self.__dict__.copy()
		if(auth == 0):
			pop_keys = ['timestamp']
		elif (auth == 1):
			pop_keys = ['index','prev_hash','nonce','timestamp',
			'hash']
		else:
			pop_keys = ['index','prev_hash','nonce','timestamp',
			'hash','uidx','subject_code','fac_code']
		[details.pop(key) for key in pop_keys]
		return details


if __name__ == '__main__':
	# Sample block to verify the working of above class
	details = {}
	details['name'] = 'Ram'
	details['dob'] = '01-11-1998'
	details['uidx'] = 876304952623
	details['acad_yr'] = '2022-23'
	details['course_start'] = '01-08-2022'
	details['course_end'] = '25-11-2022'
	details['subject'] = 'Foundations of educational technology'
	details['subject_code'] = 'ET60062'
	details['marks'] = 85.8
	details['remarks'] = 'None'
	details['inst_name'] = 'IIT Kharagpur'
	details['inst_code'] = 'WB000001'
	details['fac_code'] = '16AT17483'
	details['standard'] = 'Btech - 4'
	stu = Block(0,details,time.time(),None)
	auths = [0,1,2]
	for auth in auths:
		print(stu.return_details(auth))
	print(details)