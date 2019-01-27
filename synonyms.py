import config
import unirest
import json 
import string
import syllablecount as sc
import random

TOKEN = config.words_api_token
URL = "https://wordsapiv1.p.rapidapi.com/words/{}/synonyms"
header_name = "X-RapidAPI-Key"

raw_sentence = "My best friend is a book, that doesn't give me a weird look."

sentence = raw_sentence.translate(string.maketrans("",""), string.punctuation)
sentence = sentence.lower()
chop_sentence = raw_sentence
new_sentence = ""

excluded_words = [ "the", "me", "i", "you", "is", "with", "it", "my", "of", "a", "that", "to", "have", "are", "we", "our", "be", "am", "they", "he", "she", "been", "being", "have", "am"]

all_words = sentence.split()
dedup_words = []
place = 0

for unique_word in all_words:
	if unique_word not in excluded_words:
		if unique_word not in dedup_words:
			dedup_words.append(unique_word)

print raw_sentence

for word in dedup_words:
	current_sylco = sc.sylco(word)
	new_word = word
	new_sylco = current_sylco
	response = unirest.get(URL.format(word), headers={header_name: TOKEN})
	jsr = json.loads(response.raw_body)
	#print word
	for k,v in jsr.items():
		if k == "synonyms":
			#print v
			for synonym in v:
				if ' ' not in synonym:
					test_sylco = sc.sylco(synonym)
					if test_sylco > new_sylco:
						new_sylco = test_sylco
						new_word = synonym
					elif test_sylco == new_sylco:
						if random < .5:
							new_sylco = test_sylco
							new_word = synonym
	if new_word != word:
		place = chop_sentence.find(word)
		new_sentence += chop_sentence[0:place]
		place += len(word)
		chop_sentence = chop_sentence[place:]
		#print new_word
		new_sentence += new_word
		#print new_sentence
		
new_sentence += chop_sentence
print new_sentence

							
# fixes needed
# - look at instances of a/an before the word, check for change in vowel and if found switch
# - Need to check the case of the first letter of the old word and match that in the new.
