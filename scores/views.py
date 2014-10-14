import feedparser

from django.shortcuts import render
from scores.models import Entry

def display_scores(request):

	# current entries
	stored_entries = [e.e_id for e in Entry.objects.all()]

	# hit NYT rss feed
	d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')

	new_entries = []
	for e in d.entries:
		if not e.id in stored_entries:

			new_entry = Entry(
				title=e.title,
				summary=e.summary,
				author=e.author,
				link=e.link,
				e_id=e.id,
			)

			score = None
			## figure out score and then
			## add it to model


