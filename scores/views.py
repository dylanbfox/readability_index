from django.shortcuts import render
from scores.models import Entry

def display_scores(request):

	# current entries
	# stored_entries = [e.e_id for e in Entry.objects.all()]

	# hit NYT rss feed
	d = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')

	new_entries = []

	for e in d.entries:
		response = urllib.urlopen(d.entries[0].link)
		html = response.read()
		soup = BeautifulSoup(html)
		para_nodes = soup.find_all('p')

		story_text = []
		for p in para_nodes:
			if 'cnn_storypgraphtxt' in p.get('class', ''):
				story_text.append(p.getText())

		raw_story_text = ' '.join(story_text)
		# print raw_story_text

		## create sentences
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		story_sents = sent_detector.tokenize(raw_story_text)
		sent_counts = [len(PunktWordTokenizer().tokenize(sent))
						for sent in story_sents]

		wps = sum(sent_counts) / len(sent_counts)

		## create words
		# out of box tokenizer doesn't include puncitation,
		# so we can easily filter it out
		story_words = nltk.word_tokenize(raw_story_text)
		story_words = [w for w in story_words if re.search(r'\w', w)]
		word_counts = [len(w) for w in story_words]

		lpw = sum(word_counts) / len(word_counts)

		score = 4.71 * lpw + 0.5 * wps - 21.43

		print score
		print round(score)



