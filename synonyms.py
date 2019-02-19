import config
import unirest
import json 
import string
import syllablecount as sc
import random
import nltk
from pattern.en import pluralize
import inflect

dict_token = config.mw_dict_api_token
thes_token = config.mw_thes_api_token
# URL = "https://wordsapiv1.p.rapidapi.com/words/{}/synonyms"
URL = "https://dictionaryapi.com/api/v3/references/{}/json/{}?key={}"
dict = "collegiate"
thes = "thesaurus"

# raw_sentence = "My best friend is a book, that doesn't give me a weird look."
raw_sentence = "I am taking a test.  This will test my intelligence.  I am using this testing data to measure the effectiveness of the software.  I failed all the tests."

print raw_sentence
token_sentence = nltk.word_tokenize(raw_sentence)
print nltk.pos_tag(token_sentence)

print pluralize('test')
print pluralize('child')
print pluralize('children')
print pluralize('goose')

p = inflect.engine()

print p.singular_noun('child')
print p.singular_noun('children')
print p.plural('asparagus', 1)
print p.plural('asparagus', 2)
print p.singular_noun('sheep')
print p.plural_noun('sheep')

response = unirest.get(URL.format(thes,"children",thes_token))
jr = json.loads(response.raw_body)
print json.dumps(jr, indent=1)

# re-write with these steps
	# parse words
	# if punctuation, just append
	# if this word contains ', append this word
	# if next word contains ', append this word with a space before
	# if the word is a noun, verb, adjective, or adverb of the types listed
		# lookup synonym that matches the part of speech
		# Look at all synonym lists for that pos_tag
		# Pick a random one that has more syllables
		# Noun Only - If base is NNS and new is NN then pluralize the return
		# append new word to text string with a leading space
	# else, append this word with a space before

# Nouns - NN, NNS
# Verbs - VB, VBG, VBN
# Adjectives - JJ, JJR, JJS
# Adverbs - RB, RBR, RBS

#sentence = raw_sentence.translate(string.maketrans("",""), string.punctuation)
#sentence = sentence.lower()
#chop_sentence = raw_sentence
#new_sentence = ""

#excluded_words = [ "the", "me", "i", "you", "is", "with", "it", "my", "of", "a", "that", "to", "have", "are", "we", "our", "be", "am", "they", "he", "she", "been", "being", "have", "am"]

#all_words = sentence.split()
#dedup_words = []
#place = 0

#for unique_word in all_words:
#	if unique_word not in excluded_words:
#		if unique_word not in dedup_words:
#			dedup_words.append(unique_word)

#print raw_sentence

#for word in dedup_words:
#	current_sylco = sc.sylco(word)
#	new_word = word
#	new_sylco = current_sylco
#	response = unirest.get(URL.format(thes,word,thes_token))
#	print response.raw_body
	#jsr = json.loads(response.raw_body)
	#print word
	#for k,v in jsr.items():
	#	if k == "synonyms":
	#		#print v
	#		for synonym in v:
	#			if ' ' not in synonym:
	#				test_sylco = sc.sylco(synonym)
	#				if test_sylco > new_sylco:
	#					new_sylco = test_sylco
	#					new_word = synonym
	#				elif test_sylco == new_sylco:
	#					if random < .5:
	#						new_sylco = test_sylco
	#						new_word = synonym
	#if new_word != word:
	#	place = chop_sentence.find(word)
	#	new_sentence += chop_sentence[0:place]
	#	place += len(word)
	#	chop_sentence = chop_sentence[place:]
	#	#print new_word
	#	new_sentence += new_word
	#	#print new_sentence
		
#new_sentence += chop_sentence
#print new_sentence

							
# fixes needed
# - look at instances of a/an before the word, check for change in vowel and if found switch
# - Need to check the case of the first letter of the old word and match that in the new.


