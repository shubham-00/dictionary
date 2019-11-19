from django.shortcuts import render

import json
from difflib import get_close_matches

dictionary = json.load(open('Dictionary/data.json'))

def index(request):
	return render(request, 'index.html')



def meaning(request):
	word = request.GET.get('word', " ")
	word = word.lower()
	if word in dictionary:
		meaning = dictionary[word]
	else:
		similar_words = get_close_matches(word, dictionary.keys(), n = 20, cutoff = 0.5)
		if len(similar_words) == 0:
			meaning = ["Sorry, no matches found!"]
		else:
			meaning = ["Word not found!\nPlease check for the similar words: "] + similar_words

	ans = ''
	for i in meaning:
		ans += i + "\n"

	data = { 'ans' : ans}
	return render(request, 'meaning.html', data)
