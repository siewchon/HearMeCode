#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Challenge Level: Beginner
# Background: You have a text file with all of the US state names:
# states.txt: See section_07_(files).
#
text_file = "..\static\states.txt"

# You also have a spreadsheet in comma separated value (CSV) format, state_info.csv. See also section_07_(files)
# state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population
#
state_info_csv = "..\static\state_info.csv"

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py
#
# read the states text file into the states string
with open(text_file, "r") as fstream:
	states = fstream.readlines()

fstream.close()

print	

# output the state info into a select dropdown list

print "<select name='USStates' id='USStates'>"
for idx, state in enumerate(states):
	states[idx] = state.rstrip('\n').split('\t')
	print "<option value='{0}'>{1}</option>".format(states[idx][0], states[idx][1])
print "</select>"

print

# Challenge 2: Save the HTML as states.html instead of printing it to screen.
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.
#
out_file = "..\static\states.html"
html = "<!DOCTYPE html>\n<html><head><title>HMC Python File: States</title>\n"
html += "<script>\n"
html += "function jumpTo(e) {\n"
html += "   location.href = '#' + encodeURI(e); \n"
html += "}\n"
html += "</script>\n"
html += "</head>\n"
html += "<body>\n"
html += "<p>\n"
html += "<h2>USA states:</h2>\n"
html += "<select name=\"USStates\" id=\"USStates\" onChange=\"javascript: jumpTo(this.options[this.selectedIndex].text);\">\n"
for idx, state in enumerate(states):
	html += "<option value='{0}'>{1}</option>\n".format(state[0], state[1].title()) # need the .title() to make all name only the first letter is uppercase 

html += "</select>\n"
html += "<i>note: Palau is not in the table below.</i>\n"
html += "</p>\n"
#html += "</body></head></html>"
#print html
with open(out_file, 'w') as out_stream:
	out_stream.write(html)
out_stream.close()
	
# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.
# Sample output:
# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>
#
# retrieve the data from the state_info.csv spreadsheet
csv_file = "..\static\state_info.csv"
with open(csv_file, 'r') as inStream:
	state_info = inStream.readlines()
#print state_info[1:]

# then write and append the info retrieved from state_info.csv into the .html file
html2 = "<hr />\n"
html2 += "<table border='1'>\n"
#[['Population Rank in 50 States,State,Population Estimate,US House Seats,Percent of Total population']...]
for idx, info in enumerate(state_info[1:]):
	state_info[idx] = info.rstrip('\n').split(',')  # get list of list
	html2 += "<tr><td colspan='2'><a id='{}'>{}</a></td></tr>\n".format(state_info[idx][1].title(), state_info[idx][1])
	html2 += "<tr><td>Rank: {}</td><td>Percent: {}</td></tr>\n".format(state_info[idx][0], state_info[idx][4])
	html2 += "<tr><td>US House Members: {}</td><td>Population: {}</td></tr>\n".format(state_info[idx][3], state_info[idx][2])
html2 += "</table>\n"
html2 += "</body></html>"
# note: the id in the <a> tag is title() so that the first letter of ea word is uppercase; this is needed because the name in the dropdown list (eg: District Of Columbia) has to match the name in the table (eg: District of Columbia) else can't jump to the selected state in the table

# append html to existing .html file
with open(out_file, 'a') as outStream:
	outStream.write(html2)
outStream.close()

# Question: States that have no ranking display a special character instead of the '-' hyphen character in the browser; see line 95
# District of Columbia
# Rank: â€”	Percent: 0.19%
# US House Members: 1 (non voting)	Population: 646449

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.

