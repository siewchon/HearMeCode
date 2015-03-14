# Challenge Level: Advanced
# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
# You have two spreadsheets in CSV (comma separated value) format:
# all_employees.csv: See section_07_(files). Contains all of the employees in your organization and their contact info.
# Columns: name, email, phone, department, position
# survey.csv: See section_07_(files). Contains info for employees who have completed a survey. Not all employees have completed the survey.
# Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two. When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv & surveys.csv.
# Sample output:
# Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234
#
# open all_employees.csv and assign to a file handler:
f_all_employees = "../static/all_employees.csv"
with open(f_all_employees, "r") as f_handler:
	all_employees = f_handler.readlines();
#print all_employees
#print
for idx, employee in enumerate(all_employees):
	all_employees[idx] = employee.rstrip('\n').split(',')  #remove the EOF at the end of ea employee string then split the data into a list and re-assign the employee list back to the original all_employees list for easier data manipulation later
#print all_employees
#print

# open survey.csv and assign to another file handler:
f_survey = "../static/surveys.csv"
with open(f_survey, "r") as f_handler:
	surveys = f_handler.readlines();
#print surveys
#print
for i, survey in enumerate(surveys):
	surveys[i] = survey.rstrip('\n').split(',')
#print surveys
#print

# loop all_employees (key: email) then loop survey inside the all_employee loop and compare
# if match (key: email) found
#	output the info of this employee: name, email, phone, department, position, twitter, github
title_list = all_employees[0] + surveys[0][1:]	#collect all col title into one list with only one email addr taken from the all_employees file
#print title_list
for employee in all_employees[1:]:	#first row is a title row, skip it
	for survey in surveys[1:]:		#first row is a title row, skip it
		if (employee[1] == survey[0]):	#compare their email addresses
			temp_list = employee + survey[1:]	#combine both list into one list with only all those fields I want to output
			#print temp_list
			for idx, data in enumerate(temp_list):
				print "{0}: {1}".format(title_list[idx],data)
			print
print


# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github
#
out_file = "../static/new_all_employees.csv"
empty_list = ['','']
new_all_employees = ''

for employee in all_employees:
	match = False
	for survey in surveys:	
		if (employee[1] == survey[0]):
			match = True
			break
			
	if (match):
		new_all_employees += ",".join(employee + survey[1:]) + "\n"
	else:
		new_all_employees +=  ",".join(employee + empty_list) + "\n"

print new_all_employees

with open(out_file, "w") as f_object:
	f_object.write(new_all_employees)

# f_object is close automatically once it exited the with statement, so explicitly calling file's close() is not necessary
