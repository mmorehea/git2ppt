import os
import sys
import code
import numpy as np
import subprocess
from pptx import Presentation

class Commit(object):
	def __init__(self, author, date, commit_message):
		self.author = author
		self.date = date
		self.commit_message = commit_message

def getCommits(path):
	os.chdir(path)
	s = 'git whatchanged --since="30 days ago" > commits.txt'
	subprocess.call(s, shell=True)


def buildCommits():

	with open("commits.txt", "r") as f:
	    content = f.readlines()

	lines = [line.rstrip('\n') for line in content]

	commit = ""
	author = ""
	message = ""
	date = ""
	first = 0
	allCommits = []

	for each in lines:
		if len(each) == 0:
			continue
		if each.split()[0] == 'commit':
			if first != 0:
				com = Commit(author, date, message)
				allCommits.append(com)
				commit = ""
				author = ""
				message = ""
				date = ""
			else:
				commit = each
				first = 1
		elif each.split()[0] == 'Author:':
			author = each
		elif each.split()[0] == 'Date:':
			date = each
		elif each[0] == ':':
			continue
		else:
			message += each + ' '
	return allCommits

def filterCommits(allCommits, authorName):
	filteredCommits = []
	for each in allCommits:
		if authorName in each.author:
			filteredCommits.append(each)
	return filteredCommits

def printCommits(allCommits):
	for each in allCommits:
		print each.author
		print each.date
		print each.commit_message
		print " "
		print " "

def buildPPTX(commits):
	prs = Presentation()
	title_slide_layout = prs.slide_layouts[0]
	slide = prs.slides.add_slide(title_slide_layout)
	title = slide.shapes.title
	subtitle = slide.placeholders[1]

	title.text = "Monthly Presentation"
	subtitle.text = "Using git2ppt!"

	prs.save('test.pptx')

	for ii,each in enumerate(commits):
		print ii
		bullet_slide_layout = prs.slide_layouts[5]
		slide = prs.slides.add_slide(bullet_slide_layout)
		shapes = slide.shapes
		title = slide.shapes.title
		title.text = each.commit_message


	prs.save('test.pptx')


#gitCommits()
allCommits = buildCommits()
filtered = filterCommits(allCommits, "Michael")

printCommits(filtered)
buildPPTX(filtered)
