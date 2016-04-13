import nltk
import re
from Date import Date
class Letter:

	def __init__(self, content, letterPath):
		self.content = content
		self.m_to = ""
		self.m_from = ""
		self.m_numberOfWords = -1
		self.m_letterPath = letterPath
		self.m_numberOfWordsWithoutStopWords = -1
		self.m_date = Date("test date 1.4.1990")
	
	
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
		if (withStopWords == True && self.m_numberOfWords == -1) || (withStopWords == False && m_numberOfWordsWithoutStopWords == -1):
			numberOfWords = prosessor.getNumberOfWords(self.m_letterPath, withStopWords)
		if withStopWords:
			self.m_numberOfWords = numberOfWords
		else:
			self.m_numberOfWordsWithoutStopWords = numberOfWords
		return 
		
			
l = Letter("hey")
print(l.getFromWhomTheLetterIs())
print(l.getToWhomTheLetterIs())
		


f = open('letters//letters_to_sara.txt',encoding='utf-8')
letter = ""
for line in f:
	if "* * *" in line:
		break
	line = re.sub(r'<.*?>' ,'', line)
	letter += line
	
tokens = nltk.word_tokenize(letter)
punctuationMarks = ['.', ',', '?', '[', ']', '+', "-", '!', "'", ')', '(', "``", "''", '...']
tokens = list(filter(lambda a : a not in punctuationMarks, tokens))
print(tokens)
print(letter)

f.close()
