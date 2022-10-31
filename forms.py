from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class InputData(FlaskForm):
	name = StringField('Name')
	uidx = StringField('Aadhar number')
	dob = StringField('Date of birth')
	standard = StringField('Standard')
	acad_yr = StringField('Academic Year')
	course_start = StringField('Course start date')
	course_end = StringField('Course end date')
	subject = StringField('Subject')
	subject_code = StringField('Subject Code')
	marks = StringField('Marks Obtained')
	remarks = StringField('Any Remarks')
	inst_name = StringField('Institute Name')
	inst_code = StringField('Institute Code')
	fac_code = StringField('Faculty Code')
	submit = SubmitField('Submit')