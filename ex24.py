print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


# start_point = 10000
# beans, jars, crates = secret_formula(start_point)

# print "With a starting point of: %d" % start_point
# print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# start_point = start_point / 10

# print "We can also do that this way:"
# print "We'd have %d beans, %d jars and %d crates." %secret_formula(start_point)

# Sarahs-Mac:learn-python-the-hard-way SarahS$ python ex24.py
# Let's practice everything.
# You'd need to know 'bout escapes with \ that do
#  newlines and 	 tabs.
# --------------

# 	The lovely world
# with logic so firmly planted
# cannot discern
#  the needs of love
# nor comprehend passion from intuition
# and requires an explanation

# 		where there is none.

# --------------
# This should be five: 5
# With a starting point of: 10000
# We'd have 5000000 beans, 5000 jars, and 50 crates.
# We can also do that this way:
# We'd have 500000 beans, 500 jars and 5 crates.