"""
DS Assignment on MPI - Q1 Tokenization
"""

import nltk
import sys

def parse_data(path):
	"""
	Pass the path to the file to parse
	"""
	#path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt')
	raw = open(path, 'rU').read()
	words = nltk.word_tokenize(raw)
	words = [x.lower().strip() for x in words]
	return sorted(words)

def read_stop():
	"""
	returns: stop_words
	None of the words returned from this function should be counted
	"""

	stop_words = []
	f = open('stopwords.txt', 'r')
	while True:
		l = f.readline()
		if not l:
			break
		else:
			l = l.split("\n")
			stop_words.append(l[0])
	
	punctuation = [',', '.', '!', '?', ';', '-', '(', ')', \
					'{', '}', '[', ']', '<', '>', '/', ':', \
					'+', '-', '=', '*', '@', '$', '#', '%', \
					'--', "'s", "''", '""', "``", "'", '"', \
					"`", '~', "_"]

	for i in punctuation:
		stop_words.append(i)

	return stop_words
