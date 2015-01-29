# L1E1: Peanut Butter Jelly Time!

qty_slice_bread = input("How much bread do you have? ")	
qty_peanut_butter = input("How much peanut butter do you have? ")
qty_jelly = input("How much jelly do you have? ")

if qty_slice_bread < 2 or qty_peanut_butter < 1 or qty_jelly < 1:
	if qty_slice_bread < 2:
		missing_ingredient = "bread"
	elif qty_peanut_butter < 1:
		missing_ingredient = "peanut butter"
	else:
		missing_ingredient = "jelly"
	print "Looks like I don't have a lunch today, {} is missing.".format(missing_ingredient)
elif qty_slice_bread >= 2 and qty_peanut_butter >= 1:
	qty_sandwich = qty_slice_bread / 2
		
	if	qty_jelly < 1:
		print "I can only make peanut butter sandwich."
	elif qty_peanut_butter > qty_jelly:
		num_PBJ = qty_peanut_butter / qty_jelly
		if qty_sandwich > num_PBJ:
			num_PB = qty_sandwich - num_PBJ
			print "I can make {0} peanut butter & jelly sandwich and {1} peanut butter sandwich".format(num_PBJ, num_PB)
	else:
		#qty_sandwich = qty_slice_bread / 2
		print "I can make {0} sandwiches".format(qty_sandwich)

		bread_is_odd = qty_slice_bread % 2
		peanut_butter_is_odd = qty_peanut_butter % 2
		jelly_is_odd = qty_jelly % 2
		if (bread_is_odd and peanut_butter_is_odd and jelly_is_odd):
			print "I can also make an open-face sandwich."
		
else:
	print "I can make a peanut butter and jelly sandwich."

