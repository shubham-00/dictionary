# Shubham Patel
# github.com/shubham-00
# Open to be hired
# Contact for projects

import json

from difflib import get_close_matches


def translate(word):
	word = word.lower()

	if word in dictionary:
		return dictionary[word]

	else:
		similar_words = get_close_matches(word, dictionary.keys(), n = 10, cutoff = 0.8)	# n => Number of words it may return at max	# cutoff => Words should match atleast cutoff or more

		if len(similar_words) == 0:
			return "Sorry, word doesn't exist in the dictionary"

		else:
			print('Sorry, cannot find that word, check out similar words.')
			return similar_words


dictionary = json.load(open('data.json'))
wordInput = input('Enter a word: ')
answer = translate(wordInput)

for i in list(answer):
	print(i, end = '\n\n')

while True:
	exit = input('Do you wan to continue? (Y/N): ').lower()
	if exit == 'n':
		break;

	elif exit == 'y':
		wordInput = input('Enter a word: ')
		answer = translate(wordInput)
		for i in list(answer):
			print(i, end = '\n\n')

	else:
		print('Sorry, cannot understand')



# Shubham Patel
# github.com/shubham-00
# Open to be hired
# Contact for projects
