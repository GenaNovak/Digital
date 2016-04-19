import nltk
import re
from Date import Date
from WordProsessor import WordProsessor
from CSVHandler import CSVHandler

class Letter:

	def __init__(self, content, letterPath):
		self.m_content = content
		self.m_to = None
		self.m_from = None
		self.m_numberOfWords = None
		self.m_letterPath = letterPath
		self.m_numberOfWordsWithoutStopWords = None
		self.m_date = None



	@property
	def m_numberOfWords(self):
		if self._m_numberOfWords == None:
			self._m_numberOfWords = self.getNumberOfWords(True)
		return self._m_numberOfWords

	@m_numberOfWords.setter
	def m_numberOfWords(self, value):
		self._m_numberOfWords = value

	@property
	def m_numberOfWordsWithoutStopWords(self):
		if self._m_numberOfWordsWithoutStopWords == None:
			self._m_numberOfWordsWithoutStopWords = self.getNumberOfWords(False)
		return self._m_numberOfWordsWithoutStopWords

	@m_numberOfWordsWithoutStopWords.setter
	def m_numberOfWordsWithoutStopWords(self, value):
		self._m_numberOfWordsWithoutStopWords = value

	@property
	def m_date(self):
		if self._m_date == None:
			self._m_date = Date(self.m_content)
		return self._m_date

	@m_date.setter
	def m_date(self, value):
		self._m_date = value

	@property
	def m_to(self):
		if self._m_to == None:
			self._m_to = self.getToWhoTheLetterIs(self.m_content)
		return self._m_to

	@m_to.setter
	def m_to(self, value):
		self._m_to = value

	@property
	def m_from(self):
		if self._m_from == None:
			self._m_from = self.getFromWhoTheLetterIs(self.m_content)
		return self._m_from

	@m_from.setter
	def m_from(self, value):
		self._m_from = value

	def getNumberOfWords(self, withStopWords):
		prosessor = WordProsessor()
		numberOfWords = prosessor.getNumberOfWords(self.m_letterPath, withStopWords)
		return numberOfWords


	#find to who the letter is. the algorithem assumes that the first word in the first line after the date contains the name.
	def getToWhoTheLetterIs(self, str):
		lines = str.splitlines()
		index = 0
		for line in lines:
			if self.m_date.m_dateStr in line:
				words = lines[index + 1].split()
				return words[0]
			index +=1

	#find from who the letter is. the algorithem assumes that the last line with only one word contains the name
	def getFromWhoTheLetterIs(self, str):
		lines = str.splitlines()
		index = -1
		while index + len(lines) >= 0:
			words = lines[index].split()
			if len(words) == 1 and "\n" not in words[0]:
				return words[0]
			index -= 1
		return ""

import glob



letters = []
prosessor = WordProsessor()
for file in glob.glob("letters/*.txt"):
	letters.append(Letter(prosessor.getText(file), file))

x = CSVHandler("test.csv", ["Date", "To", "From",  "Number of words", "Number of words(with stop words)"])
x.writeLines(letters)
