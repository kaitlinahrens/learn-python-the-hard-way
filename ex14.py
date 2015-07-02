from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# sarahs-mac:learn-python-the-hard-way SarahS$ python ex14.py kaitlin
# Hi kaitlin, I'm the ex14.py script.
# I'd like to ask you a few questions.
# Do you like me kaitlin?
# > Yes
# Where do you live kaitlin?
# > Fayetteville
# What kind of computer do you have?
# > Dell, for now

# Alright, so you said 'Yes' about liking me.
# You live in 'Fayetteville'. Not sure where that is.
# And you have a 'Dell, for now' computer. Nice.