from __future__ import division

import feedparser

from django.shortcuts import render
from django.http import HttpResponse

from scores.models import Entry
from scores.utils import get_paras, get_raw_story_text
from scores.utils import get_story_sents, get_story_words
from scores.utils import calc_wps, calc_lpw, calc_score

def display_scores(request):
	context_dict = {}

	# current entries
	stored_entry_ids = [e.e_id for e in Entry.objects.all()]

	# hit NYT rss feed
	d = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')

	new_entries = []
	for e in d.entries[:15]:
		if not e.id in stored_entry_ids:

			paras = get_paras(e)
			raw_text = get_raw_story_text(paras)
			story_sents = get_story_sents(raw_text)
			story_words = get_story_words(raw_text)
			wps = calc_wps(story_sents)
			lpw = calc_lpw(story_words)
			raw_score = calc_score(wps, lpw)
			rounded_score = round(raw_score)

			new_entry = Entry(
				title = e.title,
				summary = e.summary,
				link = e.link,
				e_id = e.id,
				raw_score = raw_score,
				rounded_score = rounded_score,
				wps = wps,
				lpw = lpw
			)

			new_entries.append(new_entry)

	Entry.objects.bulk_create(new_entries)

	entries = Entry.objects.all()
	context_dict['entries'] = entries

	return render(request, "scores/scores.html", context_dict)





