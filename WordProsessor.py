import nltk
import re
import os

class WordProsessor:
	def __init__(self):
		self.m_punctuationMarks = ['.', ',', '?', '[', ']', '+', "-", '!', "'", ')', '(', "``", "''", '...']
		self.m_namesRivka = ["רבק"]
		self.m_namesSara = ["שרה", "שרת", "שׂרת"]
		self.m_specialCities = ["בין יפו וחדרה"]
		self.m_cities = ["חדרה", "יפו", "GRAND HOTEL D'ORIENT", "חיפה", "זכרון-יעקב", "דמשק", "עתלית", "קאקוּן", "קאקוּן", "אלכסנדריה"]
		self.m_knownNamesFrom = ["סַלים", "אבשלום", "סַלִים", " אבשלום."]
		self.m_stopWords = ['אני','את',
								'אתה',
								'אנחנו',
								'אתן',
								'אתם',
								'הם',
								'הן',
								'היא',
								'הוא',
								'שלי',
								'שלו',
								'שלך',
								'שלה',
								'שלנו',
								'שלכם',
								'שלכן',
								'שלהם',
								'שלהן',
								'לי',
								'לו',
								'לה',
								'לנו',
								'לכם',
								'לכן',
								'להם',
								'להן',
								'אותה',
								'אותו',
								'זה',
								'זאת',
								'אלה',
								'אלו',
								'תחת',
								'מתחת',
								'מעל',
								'בין',
								'עם',
								'עד',
								'נגר',
								'על',
								'אל',
								'מול',
								'של',
								'אצל',
								'כמו',
								'אחר',
								'אותו',
								'בלי',
								'לפני',
								'אחרי',
								'מאחורי',
								'עלי',
								'עליו',
								'עליה',
								'עליך',
								'עלינו',
								'עליכם',
								'לעיכן',
								'עליהם',
								'עליהן',
								'כל',
								'כולם',
								'כולן',
								'כך',
								'ככה',
								'כזה',
								'זה',
								'זות',
								'אותי',
								'אותה',
								'אותם',
								'אותך',
								'אותו',
								'אותן',
								'אותנו',
								'ואת',
								'את',
								'אתכם',
								'אתכן',
								'איתי',
								'איתו',
								'איתך',
								'איתה',
								'איתם',
								'איתן',
								'איתנו',
								'איתכם',
								'איתכן',
								'יהיה',
								'תהיה',
								'היתי',
								'היתה',
								'היה',
								'להיות',
								'עצמי',
								'עצמו',
								'עצמה',
								'עצמם',
								'עצמן',
								'עצמנו',
								'עצמהם',
								'עצמהן',
								'מי',
								'מה',
								'איפה',
								'היכן',
								'במקום שבו',
								'אם',
								'לאן',
								'למקום שבו',
								'מקום בו',
								'איזה',
								'מהיכן',
								'איך',
								'כיצד',
								'באיזו מידה',
								'מתי',
								'בשעה ש',
								'כאשר',
								'כש',
								'למרות',
								'לפני',
								'אחרי',
								'מאיזו סיבה',
								'הסיבה שבגללה',
								'למה',
								'מדוע',
								'לאיזו תכלית',
								'כי',
								'יש',
								'אין',
								'אך',
								'מנין',
								'מאין',
								'מאיפה',
								'יכל',
								'יכלה',
								'יכלו',
								'יכול',
								'יכולה',
								'יכולים',
								'יכולות',
								'יוכלו',
								'יוכל',
								'מסוגל',
								'לא',
								'רק',
								'אולי',
								'אין',
								'לאו',
								'אי',
								'כלל',
								'נגד',
								'אם',
								'עם',
								'אל',
								'אלה',
								'אלו',
								'אף',
								'על',
								'מעל',
								'מתחת',
								'מצד',
								'בשביל',
								'לבין',
								'באמצע',
								'בתוך',
								'דרך',
								'מבעד',
								'באמצעות',
								'למעלה',
								'למטה',
								'מחוץ',
								'מן',
								'לעבר',
								'מכאן',
								'כאן',
								'הנה',
								'הרי',
								'פה',
								'שם',
								'אך',
								'ברם',
								'שוב',
								'אבל',
								'מבלי',
								'בלי',
								'מלבד',
								'רק',
								'בגלל',
								'מכיוון',
								'עד',
								'אשר',
								'ואילו',
								'למרות',
								'אס',
								'כמו',
								'כפי',
								'אז',
								'אחרי',
								'כן',
								'לכן',
								'לפיכך',
								'מאד',
								'עז',
								'מעט',
								'מעטים',
								'במידה',
								'שוב',
								'יותר',
								'מדי',
								'גם',
								'כן',
								'נו',
								'אחר',
								'אחרת',
								'אחרים',
								'אחרות',
								'אשר',
								'או']



	#return true if "word" is a stopword. false otherwise
	def isStopWord(self, word):
		return word in self.m_stopWords


	#return number of word with or without stopwords
	def getNumberOfWords(self, filePath, withStopWords):
		with open(filePath ,encoding='utf-8') as file:
			text = file.read()
			text = re.sub(r'<.*?>' ,'', text)
			tokens = nltk.word_tokenize(text)
			tokens = list(filter(lambda a : a not in self.m_punctuationMarks, tokens))
			if withStopWords:
				tokens = list(filter(lambda a: a not in self.m_stopWords, tokens))
			return len(tokens)

	#return a list of all words	in filePath
	def getAllWords(self, filePath):
		with open(filePath, encoding='utf-8') as file:
			text = file.read()
			text = re.sub(r'<.*?>' ,'', text)
			tokens = nltk.word_tokenize(text)
			return tokens

	#return the text in filePath
	def getText(self, filePath):
		with open(filePath, encoding='utf-8') as file:
			text = file.read()
			text = re.sub(r'<.*?>' ,'', text)
			text = re.sub(r'\[[0-9].*?\]', '', text)
			text = re.sub(",", " , ", text)
			text = re.sub("-", " - ",text)
			text = self.removeEmptyLine(text)
			return text

	#return an array with words that was seperated by string
	def separateTextBySpace(self, filePath):
		with open(filePath, encoding='utf-8') as file:
			text = file.read()
			text = re.sub(",", " , ", text)
			text = re.sub(". ", " . ", text)
			text = re.sub(" .", " . ", text)
			text = re.sub(".\n", " .\n", text)
			text = text.split()
			return text

	def removeEmptyLine(self, text):
		newlines = []
		lines = text.splitlines()
		for line in lines:
			line = line.strip()
			if line not in "":
				newlines.append(line)
		return "\n".join(newlines)

	def hasNumbers(inputString):
		return any(char.isdigit() for char in inputString)

	def hasPunctuationMarks(self, inputString):
		for mark in self.m_punctuationMarks:
			if mark in inputString:
				return True
		return False
