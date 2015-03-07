# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

bread = input("How many slices of bread? ")
peanut_butter = input("How much peanut_butter? ")
jelly = input("How much jelly? ")

bread = int(bread)/2
peanut_butter = int(peanut_butter)
jelly = int(jelly)

# the smallest of all three will give me the max sandwich I can make
ingredients_quantity = [bread, peanut_butter, jelly]
max_sandwich = min(ingredients_quantity)
#print "min(alist) = ", min(alist)

# this is for zip() later
ingredients = ['bread', 'peanut butter' ,'jelly']

#while (bread >= 1 or peanut_butter >= 1 or jelly >= 1):
if (bread >= 1 and peanut_butter >= 1 and jelly >= 1):
	
	i = 1
	
	while (max_sandwich >= i):
	
		print "Making sandwich #{} ".format(i)
		bread -= 1;
		peanut_butter -= 1
		jelly -= 1
		
		if (bread != 0 and peanut_butter != 0 and jelly != 0):
			print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread, peanut_butter, jelly)
		
		#max_sandwich -= 1
		i += 1
	else:
		#print "All done; only had enough bread for {} sandwiches.".format(i-1)
		for (qty, item) in zip(ingredients_quantity, ingredients):
			if (qty == max_sandwich):
				print "All done; I ran out of {}.".format(item)
				break

else:
	print "Oops, not enough ingredient to make a sandwich!"

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.
# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4
# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.
