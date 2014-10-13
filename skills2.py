import string 

string1 = "I do not like green eggs and ham. I do not do not sam i am."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
"""

def count_unique(string1):
    word_list = string1.split()
    word_dict = {}
    for word in word_list:
		word_dict[word] = word_dict.setdefault(word, 0) + 1
    return word_dict

print count_unique(string1)

"""
Bonus: do the same for a file (i.e. twain.txt)
"""

def count_unique_file(filename):
	f = open(filename)			# Open given file
	f_string = f.read()			# Read the file into a string
	f_string = f_string.replace("--"," ")	# Replace all double dashes with space (because there happen to be a lot of those in twain.txt)
	word_list = f_string.lower().split()				# Make string all lowercase then split into list of words
	for i, word in enumerate(word_list):				# Iterate over words in word_list	
		for char in word:					# Iterate over char in word
			if char in string.punctuation:			# Is that char a punctuation mark?
				word = word.replace(char,"")		# If so, then remove it from the string
				word_list[i] = word 			# Replace list item with cleaned up word

	word_dict = {}							# Create an empty dictionary for word count

	for word in word_list:						# Iterate over word list
		word_dict[word] = word_dict.setdefault(word, 0) + 1 	# Is there already a key for that word in word_dict? 
																# If not, this will create key and set value at 0 + 1
																# If so, setdefault will return current value then add 1
	return word_dict

print count_unique_file("twain.txt")

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""

def common_items(list1, list2):
	set_list1 = set(list1)		# Turn both lists into sets
	set_list2 = set(list2)		
	common = set_list1 & set_list2	# Create new set of common items that are in both lists
	common = list(common)		# Convert that set into a list
	common.sort()			
	return common

print common_items(list1,list2)

"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""

def common_items2(list1, list2):
    comparison_dict = {}
    common = []
    for word in list1:
    	comparison_dict[word] = "Yep"
    for word in list2:
    	if comparison_dict.get(word, "Nope") == "Yep":
    		common.append(word)
    common.sort()
    return common

print common_items2(list1,list2)


"""
Given a list of numbers, return list of number pairs that sum to zero
"""

def sum_zero(list1):
	pairs = []				# Create an empty list to store pairs we find
	for i in range(len(list1)):		# Iterate over numbers in list
		num = list1[i]
		rest_of_list = list1[i+1:]	# Store rest of list (after i) 

		match = next((x for x in rest_of_list if x + num == 0), "Nope")	

		if match != "Nope":
			pairs.append((num,match))

	return pairs

print sum_zero(list1)


"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    word_set = set(words)
    word_set = list(word_set)
    return word_set

print find_duplicates(words)

"""
Given a list of words, print the words in ascending order of length
"""

def word_length(words):
	len_dict = {}	# Create empty dictionary	
	for word in words:		# Iterate over word list
		word = word.lower()	# Make each word lowercase
		len_dict[word] = len(word)	# Then add word to dict with its length as the value

	word_list = len_dict.keys()						# Pull the keys from dict and put into a list
	word_list = sorted(word_list, key = lambda word: len_dict[word])	# Look up each word length in dict then sort by that

	for word in word_list:
		print word

word_length(words)

"""
Bonus: do the above function on a file instead of the list provided
Extra bonus: print the words in alphabetical order in ascending order of length
"""

def word_length_file(filename):
	f = open(filename)	# Open the given file
	text = f.read()		# Read the whole file into one long string
	text = text.replace("--"," ")	# Get rid of those pesky double dashes

	word_list = text.lower().split()	# Convert to lowercase then split it into list of words

	for i in range(len(word_list)):
		word = word_list[i]
		word = word.strip(string.punctuation)	# Strip leading/trailing punctuation from each word
		word_list[i] = word

	result = sorted(word_list, key = lambda word: len(word))	# Sort words by their length
	result.sort()	# Sort again alphabetically 

	for word in result:
		print word

word_length_file("twain.txt")
	

"""
Write a program that asks the user to type in a sentence and then
print the sentence translated to pirate.
"""

pirate_dictionary = {
	"sir": "matey",
	"hotel": "fleabag inn",
	"student": "swabbie",
	"boy": "matey",
	"madam": "proud beauty",
	"professor": "foul blaggart",
	"restaurant": "galley",
	"your": "yer",
	"excuse": "arr",
	"students": "swabbies",
	"are": "be",
	"lawyer": "foul blaggart",
	"the": "th'",
	"restroom": "head",
	"my": "me",
	"hello": "avast",
	"is": "be",
	"man": "matey"
}

def eng_to_pirate():
	message = raw_input("Yarr, what do you wish to say to your pirate mateys? ")
	message = message.split()

	for i in range(len(message)):							# iterate through words in message
		orig_word = message[i]
		word_clean = orig_word.lower().strip(string.punctuation)	# store copy of word in lowercase without punctuation
		translated = pirate_dictionary.get(word_clean, orig_word)	# translate word (if found in dict)

		if orig_word[0] in string.ascii_uppercase:			# bring back original capitalization
			translated = translated[0].upper() + translated[1:]

		if orig_word[-1] in string.punctuation:				# bring back original punctuation
			translated += orig_word[-1]

		message[i] = translated		# replace word in message list with its translation

	message = " ".join(message)		# join message list 
	print message

eng_to_pirate()

