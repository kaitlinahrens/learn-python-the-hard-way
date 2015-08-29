import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.or/words.txt"
WORDS = []

PHRASES = {
		"class %%%(%%%):":
			"Make a class named %%% that is-a %%%.",
		"class %%%(object):\n\tdef_init_(self, ***)" :
			"class %%% has-a __init__ that takes self and *** parameters.",
		"class %%%(object):\n\tdef ***(self, @@@)":
			"class %%% has-a function named *** that takes self and @@@ parameters.",
		"*** = %%%()":
			"Set *** to an instance of class %%%.",
		"***.***(@@@)":
			"From *** get the *** function, and call it with parameters self, @@@.",
		"***.*** = '***'":
			"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class name
		for word in class_names:
			result = resut.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("***", word, 1)

		results.append(result)

	return results


# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer - answer, question

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"

# Sarahs-Mac:learn-python-the-hard-way SarahS$ python ex41.py
# Traceback (most recent call last):
#   File "ex41.py", line 29, in <module>
#     for word in urlopen(WORD_URL).readlines():
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 87, in urlopen
#     return opener.open(url)
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 213, in open
#     return getattr(self, name)(url)
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 350, in open_http
#     h.endheaders(data)
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 997, in endheaders
#     self._send_output(message_body)
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 850, in _send_output
#     self.send(msg)
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 812, in send
#     self.connect()
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py", line 793, in connect
#     self.timeout, self.source_address)
#   File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 553, in create_connection
#     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
# IOError: [Errno socket error] [Errno 8] nodename nor servname provided, or not known

# i am hopelessly confused.





























