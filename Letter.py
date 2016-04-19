import nltk
import re
from Date import Date
from WordProsessor import WordProsessor

class Letter:

	def __init__(self, content, letterPath):
		self.m_content = content
		self.m_to = ""
		self.m_from = ""
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




	#return who write this letter
	def getFromWhomTheLetterIs(self):
		if self.m_from == "":
			self.m_from = "Gena"
		return self.m_from


	#return to who the letter is
	def getToWhomTheLetterIs(self):
		if self.m_to == "":
			self.m_to = "Reut"
		return self.m_to

	# not finnished
	def getNumberOfWords(self, withStopWords):
		prosessor = WordProsessor()
		numberOfWords = prosessor.getNumberOfWords(self.m_letterPath, withStopWords)
		return numberOfWords


w = WordProsessor()
text = w.getText('letters//letters_to_sara.txt')
l = Letter(text, 'letters//letters_to_sara.txt')
print(l.m_date.m_dateStr)
print(l.m_numberOfWordsWithoutStopWords)
