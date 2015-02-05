# Difficulty Level: Intermediate

# Goal: Create a program that prints out an HTML drop down menu for all 50 states

# Step 1: Define two lists, one for states and another its abbreviations
# These should all be strings, since they're names of places

ls_States_Abbreviations = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
str_States = "Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District Of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming"
ls_States = str_States.split(', ')
#print "list states are {} ".format(ls_States)

# Step 2: Create your loop
# Essentially, you're telling Python: for each state in my list: print this HTML code
# A good place to start is by printing the name of the state in the loop; after that you can add the HTML around it

print "<html>\n\
<head>\n\
<title>HMC Lesson2 Playtime: states</title>\n\
</head>\n\
<body>\n\
<p>\n\
<h2>This is my states in a select dropdown list:</h2>"
print "<select name='states'>"
for (state_abbreviation, state) in zip(ls_States_Abbreviations, ls_States):
	#print "state_abbreviation {0}, state {1} ".format(state_abbreviation, state)
	print "\t<option value='{0}'>{1}</option>".format(state_abbreviation, state)
print "</select>"
print "</p>\n\
</body>\n\
</html>"


# Step 4: Test it!
# Have Python print out the HTML code. Copy / paste it into a file, save that file as "states.html" and open that file in a web browser.
# Later, when we learn file handling, we can skip the copy/paste step.
# File handling can also let us create a file with the state names and abbreviations in it so we don't have to add it to our code.

# Your finished project should look something like: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/states.html
