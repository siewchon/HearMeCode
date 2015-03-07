# Difficulty level: Advanced

# Goal #1: Create a program that will print out a list of movie titles and a set of ratings defined below into a particular format.

# First, choose any five movies you want.
movies_titles = ['Frozen', 'Guardians of the Galaxy', 'The Avengers', 'Epic', 'Tangled']

# Next, look each movie up manually to find out four pieces of information:
	# Their parental guidance rating (G, PG, PG-13, R)
parental_rating = ['PG', 'PG-13', 'PG-13', 'PG', 'PG'] 
	# Their Bechdel Test Rating (See http://shannonvturner.com/bechdel or http://bechdeltest.com/)
bechdel_rating = [3,3,1,3,3]
	# Their IMDB Rating from 0 - 10 (See http://imdb.com/)
imdb_rating = [7.9, 9.0, 8.2, 6.7, 7.9]
	# Their genre according to IMDB
movie_genre = 	[['Adventure', 'Animation', 'Comedy'], \
				 ['Action', 'Adventure', 'Sci-Fi'], \
				 ['Action', 'Adventure', 'Sci-Fi'], \
				 ['Adventure', 'Animation', 'Family'], \
				 ['Animation', 'Comedy', 'Family'] ]
	
# After a few more lessons, you'll be able to tell Python to go out and get that information for you, but for now you'll have to collect it on your own.

# Now that you've written down each piece of information for all five of your movies, save them into variables.

# You'll need a variable for movie_titles, a variable for parental_rating, a variable for bechdel_rating, a variable for imdb_rating, and a variable for genre.

# Since you have five sets of facts about five movies, you'll want to use lists to hold these pieces of information.

# Once all of your information is stored in lists, loop through those lists to print out information with each part separated by a comma, like this:

# Example:
# Jurassic Park, PG-13, 3, 8.0, Adventure / Sci-Fi
# Back to the Future, PG, 1, 8.5, Adventure / Comedy / Sci-Fi


print "Title, Rating, Bechdel, IMDB, Genre"
for num in range (0,5):
	movie_rating = "'{title}', '{rating}', '{bechdel}', '{imdb}', '{genre}'"
	print movie_rating.format(title=movies_titles[num], rating=parental_rating[num], bechdel=bechdel_rating[num], imdb=imdb_rating[num], genre=" / ".join(movie_genre[num])) 
	
	
# Note how each piece of information is separated by a comma. This is a specific file format called the "Comma Separated Value (CSV)" format
# If you can make a CSV file, you can open it up in Excel or Numbers as a spreadsheet.

with open('movies.csv', 'w') as movie_files:

	movie_files.write("Title, Rating, Bechdel, IMDB, Genre\n")
	for num in range (0,5):

		movie_rating = "{title}, {rating}, {bechdel}, {imdb}, {genre}\n"
		str_movie = movie_rating.format(title=movies_titles[num], rating=parental_rating[num], bechdel=bechdel_rating[num], imdb=imdb_rating[num], genre=" / ".join(movie_genre[num]))
		
		movie_files.write(str_movie)
		
movie_files.close()


# When you've printed out your information like the example above, copy/paste that into a file and save it as a .csv file.
# Open that up in Excel, Numbers, or another spreadsheet program. How does it look?
# To see an example of how it should look, check out: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/movies.csv

# http://cea.balancetrak.com/lists/174/default.aspx?q=UtqR%2fFyL8Gg%3d
# http://www.akima.com/

