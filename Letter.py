import nltk
import re
from Date import Date
from WordProsessor import WordProsessor


class Letter:

	def __init__(self, content, letterPath):
		self.m_content = WordProsessor().getText(letterPath)
		self.m_to = None
		self.m_from = None
		self.m_numberOfWords = None
		self.m_letterPath = letterPath
		self.m_numberOfWordsWithoutStopWords = None
		self.m_date = None
		self.m_location = None



	@property
	def m_location(self):
		if self._m_location == None:
			self._m_location = self.getLocation()
		return self._m_location

	@m_location.setter
	def m_location(self, value):
		self._m_location = value

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

	def getLocation(self):
		prosessor = WordProsessor()
		for city in prosessor.m_specialCities:
			if city in self.m_content:
				return city
		for city in prosessor.m_cities:
			if city in self.m_content:
				return city
		return ""

	def getNumberOfWords(self, withStopWords):
		prosessor = WordProsessor()
		numberOfWords = prosessor.getNumberOfWords(self.m_letterPath, withStopWords)
		return numberOfWords


	#find to who the letter is. the algorithem assumes that the first word in the first line after the date contains the name.
	def getToWhoTheLetterIs(self, str):
		lines = self.m_content.splitlines()
		index = 0
		newIndex = 0
		numberOfLines = len(lines)
		for line in lines:
			partOfDate = "&&&"
			splitedDate = self.m_date.m_dateStr.split()
			if(len(splitedDate) > 1):
				partOfDate = splitedDate[1]
			if self.m_date.m_dateStr not in "" and (self.m_date.m_dateStr in line or line in self.m_date.m_dateStr or partOfDate in line or line in partOfDate) :
				words = lines[index + 1].split()
				for name in WordProsessor().m_namesRivka:
					if (numberOfLines > index + 1 and name in lines[index + 1]) or (numberOfLines > index + 2 and name in lines[index + 2]) or (numberOfLines > index + 3 and name in lines[index + 3]):
						return "רבקה"
				for name in WordProsessor().m_namesSara:
					if (numberOfLines > index + 1 and name in lines[index + 1]) or (numberOfLines > index + 2 and name in lines[index + 2]) or (numberOfLines > index + 3 and name in lines[index + 3]):
						return "שרה"
				if line in "3 juillet 1911":
					return "רבקה"
			index +=1
		if("rivka"  in self.m_letterPath):
			return "רבקה"
		if("sara" in self.m_letterPath):
			return "שרה"
		return ""

	#find from who the letter is. the algorithem assumes that the last line with only one word contains the name
	def getFromWhoTheLetterIs(self, str):
		prosessor = WordProsessor()
		lines = self.m_content.splitlines()
		index = -1
		while index + len(lines) >= 0:
			words = lines[index].split()
			if len(words) == 1 and "\n" not in words[0] and "]" not in words[0] and words[0] != "פ." and words[0] != "א." and prosessor.hasPunctuationMarks(words[0]) == False and words[0] in prosessor.m_knownNamesFrom:
				if(WordProsessor.hasNumbers(words[0])):
					newIndex = index - 1
					words = lines[newIndex].split()
					while(WordProsessor.hasNumbers(words[0])):
						newIndex -=1
						words = lines[newIndex].split()

					return words[0]
				return words[0]
			index -= 1
		return ""
