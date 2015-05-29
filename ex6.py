x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s' . " % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# Sarahs-Mac:learn-python-the-hard-way SarahS$ python ex6.py
# There are 10 types of people.
# Those who know binary and those who don't.
# I said: 'There are 10 types of people.'.
# I also said: 'Those who know binary and those who don't.' .
# Isn't that joke so funny?! False
# This is the left side of...a string with a right side.