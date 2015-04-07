# coding=utf-8

#! /usr/bin/python

import urllib2
from HTMLParser import HTMLParser

class Spider:
	def __init__(self):
		self.url = "http://www.mtime.com"
		self.content = ""

	def getContent(self):
		opener = urllib2.urlopen(self.url)
		self.content = opener.read()

	def parse(self):
		parser = DataParser()
		parser.feed(self.content.decode('utf-8'))
		parser.close()

class DataParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.findUpCommingSlid = False
		self.findStrong = False
		self.findIWantMovie = False

	def handle_starttag(self, tag, attrs):
		if tag == 'dl':
			for (key, value) in attrs:
				if key == 'id' and value == 'upcomingSlide':
					self.findUpCommingSlid = True
					break
		if self.findUpCommingSlid and tag == 'strong':
			self.findStrong = True
		if self.findUpCommingSlid and tag == 'li':
			for (key, value) in attrs:
				if key == 'class' and value == 'i_wantmovie':
					self.findIWantMovie = True
					break
		if self.findIWantMovie and tag == 'a':
			for (key, value) in attrs:
				if key == 'title':
					print value


	def handle_data(self, data):
		if self.findStrong:
			print data

	def handle_endtag(self, tag):
		if self.findUpCommingSlid and tag == 'dl':
			self.findUpCommingSlid = False
		if self.findStrong and tag == 'strong':
			self.findStrong = False
		if self.findIWantMovie and tag == 'li':
			self.findIWantMovie = False


if __name__ == '__main__':
	spider = Spider()
	spider.getContent()
	spider.parse()