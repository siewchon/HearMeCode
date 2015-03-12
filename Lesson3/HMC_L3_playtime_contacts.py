# Challenge Level: Beginner
# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!
# Background: You have a dictionary with people's contact information. You want to display that information as an HTML table.
contacts = {
'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },
'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}
# Goal 1: Loop through that dictionary to print out everyone's contact information.
# Sample output:
# Shannon's contact information is:
# Phone: 202-555-1234
# Twitter: @svt827
# Github: @shannonturner
# Beyonce's contact information is:
# Phone: 303-404-9876
# Twitter: @beyonce
# Github: @bey
#
# contacts is a dictionary with 3 items/keys that have another dictionary of 3 items
#
#for contact, info in sorted(contacts.iteritems()): print (type(contact), contact, type(info), info)
#print 
for contact, info in sorted(contacts.iteritems()):
	print "{0}'s contact information is:".format(contact)
	for info_detail in info.iterkeys():
		print "{0}: {1}".format(info_detail, info[info_detail])
	print
	
# Goal 2: Display that information as an HTML table.
# Sample output:
# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>
# ...
#
print 
print "<table border=\"1\">"
for contact, info in sorted(contacts.iteritems()):
	print "<tr>"
	print "<td colspan=\"3\" align=\"center\"> {} </td>".format(contact)
	print "</tr>"
	print "<tr>"
	for info_detail in info.iterkeys():
		print "<td> {0}: {1} </td>".format(info_detail, info[info_detail])
	print "</tr>"
print "</table>"


# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.
#
# note: all my static html files are stored in different directory
# example of where my files are located locally:
# my base directory is C:\hon\py27_site\test\HMC\Lesson3
# under Lesson3 are \playtime\HMC_L3_playtime_contacts.py
#							 \HMC_L3_playtime_states.py
# 					\static\contacts.csv
#						   \contacts.html
#						   \contacts_csv.html
#
html = ""
html += "<!DOCTYPE html>\n"
html += "<html><head><title>HMC Playtime: Contacts</title></head>\n"
html += "<body>\n"
html += "<table border=\"1\">\n"
for contact, info in sorted(contacts.iteritems()):
	html += "<tr>\n"
	html += "<td colspan=\"3\" style=\"text-align:center;background-color:gray;\"> {} </td>\n".format(contact)
	html += "</tr>\n"
	html += "<tr>\n"
	for info_detail in info.iterkeys():
		html += "<td> {0}: {1} </td>\n".format(info_detail, info[info_detail])
	html += "</tr>\n"
html += "</table>\n"
html += "</body></html>"
print
#print html
fstream = open("..\static\contacts.html", "w")	#this is old school style/way of opening a file
fstream.write(html)
fstream.close() 	#since not using the 'with' statement, closing file handler explicitly with close() is needed 

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).
#
with open("..\static\contacts.csv", "r") as inStream:
	contact_list = inStream.readlines()
# since I use the 'with' statement, closing file handler explicitly with close() is not necessary as the system will automatically close the file handler when the 'with' block is exited:
html = ""
html += "<!DOCTYPE html>\n"
html += "<html><head><title>HMC Playtime: Read from Contacts CSV</title></head>\n"
html += "<body>\n"
html += "<table border=\"1\">\n"
for idx, contact in enumerate(contact_list):
	contact_list[idx] = contact.rstrip('\n').split(',') 	#split the long string into list for easier manipulation of data later
	#print contact_list[idx]
	html += "<tr>\n"
	if (idx == 0): 	# this is title row
		html += "<th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th>\n".format(contact_list[idx][0],contact_list[idx][1],contact_list[idx][2],contact_list[idx][3])
	else:
		html += "<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>\n".format(contact_list[idx][0],contact_list[idx][1],contact_list[idx][2],contact_list[idx][3])
	html += "</tr>\n"	
html += "</table>\n"
html += "</body></html>"

#print html
outStream = open("..\static\contacts_csv.html", "w")
outStream. write(html)
outStream.close()

# the last 3 lines of code can also be rewritten using the 'with' statement and the call to close the file handler is not needed when using the 'with' statement as it will be closed automatically when the 'with' block is exited:
#with open("..\static\contacts_csv.html", "w") as outStream:
#	outStream.write(html)	
