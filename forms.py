from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputData(FlaskForm):
	'''
	Inherited from Flaskform class
	Used to take the input from the user
	'''
	name = StringField('Name',[DataRequired()])
	uidx = StringField('Aadhar number',[DataRequired()])
	dob = StringField('Date of birth',[DataRequired()])
	standard = StringField('Standard',[DataRequired()])
	acad_yr = StringField('Academic Year',[DataRequired()])
	course_start = StringField('Course start date',[DataRequired()])
	course_end = StringField('Course end date',[DataRequired()])
	subject = StringField('Subject',[DataRequired()])
	subject_code = StringField('Subject Code',[DataRequired()])
	marks = StringField('Marks Obtained',[DataRequired()])
	remarks = StringField('Any Remarks',[DataRequired()])
	inst_name = StringField('Institute Name',[DataRequired()])
	inst_code = StringField('Institute Code',[DataRequired()])
	fac_code = StringField('Faculty Code',[DataRequired()])
	submit = SubmitField('Submit')