contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Siew Hon"] = {
	"twitter" : "",
	"github" : "https://github.com/siewchon/HearMeCode/tree/Exercises"
}

#print contacts.items()

# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner

for contact, info in contacts.items():
	print "\n{0}:".format(contact)
	for data in info.iterkeys():
        # replace info on twitter if it's empty
		if data == 'twitter' and info[data] == '':
			info[data] = 'no twitter account'
		print "\t{0}: {1}".format(data, info[data])
		
        
