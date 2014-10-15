from __future__ import division

import feedparser
import urllib
import nltk
import re

from nltk.tokenize.punkt import PunktWordTokenizer
from bs4 import BeautifulSoup

def get_paras(entry):

	response = urllib.urlopen(entry.link)
	html = response.read()
	soup = BeautifulSoup(html)
	para_nodes = soup.find_all('p')

	return para_nodes

def get_raw_story_text(paras):

	story_text = []
	for p in paras:
		if 'cnn_storypgraphtxt' in p.get('class', ''):
			story_text.append(p.getText())

	raw_story_text = ' '.join(story_text)

	return raw_story_text

def get_story_sents(raw_text):

	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	story_sents = sent_detector.tokenize(raw_text)

	return story_sents

def calc_wps(story_sents):

	sent_counts = [len(PunktWordTokenizer().tokenize(sent))
					for sent in story_sents]

	try:
		wps = sum(sent_counts) / len(sent_counts)
	except:
		return 0 

	return wps

def get_story_words(raw_text):

	# out of box tokenizer doesn't include puncitation,
	# so we can easily filter it out
	story_words = nltk.word_tokenize(raw_text)
	story_words = [w for w in story_words if re.search(r'\w', w)]

	return story_words

def calc_lpw(story_words):

	word_counts = [len(w) for w in story_words]

	try:
		lpw = sum(word_counts) / len(word_counts)
	except:
		return 0

	return lpw

def calc_score(wps, lpw):

	if wps == 0 and lpw == 0:
		return 0
		
	score = 4.71 * lpw + 0.5 * wps - 21.43

	return score