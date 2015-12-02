import string
PATH_TO_FILE = '/home/akp/pythonera/loadWords/words.txt'

def loadWords():
	inFile = open(PATH_TO_FILE, 'r', 0)
	line = inFile.readline()
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

loadWords()


def loadWords2():
	try:
		inFile = open(PATH_TO_FILE, 'r', 0)
	except IOError:
		print "The wordlist doesn't exist; using some fruits for now"
		return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
	line = inFile.readline()
	wordlist = string.split(line, ',')
	print "  ", len(wordlist), "words loaded."
 	return wordlist
PATH_TO_FILE = '/home/akp/pythonera/loadWords/words2.txt'
loadWords2()
PATH_TO_FILE = '/home/akp/pythonera/loadWords/words.txt'
loadWords2()
