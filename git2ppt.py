import os
import sys
import code
import numpy as np

class Commit(object):
	def __init__(self, author, date, commit_message):
		self.author = author
		self.date = date
		self.commit_message = commit_message



with open("try.txt", "r") as f:
    content = f.readlines()

lines = [line.rstrip('\n') for line in content]



def buildCommits(lines):
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
		print ' '.join(each.commit_message.split())
		print " "
		print " "


allCommits = buildCommits(lines)
filtered = filterCommits(allCommits, "Michael")

printCommits(filtered)
