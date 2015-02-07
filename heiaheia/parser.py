#!/usr/bin/env python

'''parser.py'''

import re
import feedparser
from time import mktime
from models import Workout

def _parse_title(regex, title):
	'''Parse title string with regular expression'''
	match = re.search(regex, title)
	if match is not None:
		return match.group(0).strip()
	return '0'#Sport should match always so zero can be returned for the distance and duration

def _parse_entry(entry):
	'''Parse workout data from the entry'''
	title = entry.title
	sport = _parse_title('[a-zA-Z\s]+', title)
	distance = float(_parse_title('[\.|\d]+\skm', title).split(' ')[0])
	duration_h = int(_parse_title('\d+\sh', title).split(' ')[0])
	duration_m = int(_parse_title('\d+\smin', title).split(' ')[0])
	duration_s = int(_parse_title('\d+\ss', title).split(' ')[0])
	duration = (duration_h*3600) + (duration_m*60) + duration_s
	date = mktime(entry.published_parsed)
	return Workout(sport=sport, distance=distance, duration=duration, date=date)

def _parse_entries(entries):
	'''Parse entries'''
	workouts = []
	for entry in entries:
		workouts.append(_parse_entry(entry))
	return workouts

def _get_entries(feed):
	'''Get entries from the feed'''
	return feed.entries

def _get_feed(url):
	'''Get RSS feed'''
	return feedparser.parse(url)


def parse_feed(url):
	'''Parse RSS feed
	:param url: URL for the RSS feed
	:returns: List of Workout objects
	'''
	feed = _get_feed(url)
	entries = _get_entries(feed)
	workouts = _parse_entries(entries)
	return workouts
