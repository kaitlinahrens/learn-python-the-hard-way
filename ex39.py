# create a mapping of state to abbreviation
states = [
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
]

# creates a basic set of states and some cities in them
cities = [
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
]

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items()
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items()
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time 
print '-' * 10
for state, abbrev in states.items()
	print "%s state is abbreviated %s and has city %s" %(
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', none)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city


#every list that I created at the top gave me an invalid syntax error at the colon. I even took the first list out and it did the same
#thing at line 12. It wouldn't let me run the program. There are colons in the exercise. I dunno.









