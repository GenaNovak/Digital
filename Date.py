from datetime import datetime
from WordProsessor import WordProsessor
import re

class Date:
	def __init__(self, str):
		self.m_supportedDateFormats = ["%d.%m.%Y", "%d.%m.%y", "%Y %B", "%Y %d %B"]
		self.m_specialDates = ["3 Juillet 1911", "1 Janvier 1913", "1913, 22 juin", "1913 22 juin", "juillet 1911", "דסוכות א'"]
		self.m_HebrewMothsList = ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יולי", "אוגוסט", "ספטמבר", "אוקטובר", "נובמבר", "דצמבר"]
		self.m_dateStr = self.getDateFromString(str)

	def getDateFromString(self, str):
		str = re.sub(",", " , ", str)
		words = str.split()
		date = ""
		for dateFormat in self.m_supportedDateFormats:
			for word in words:
				try:
					date = datetime.strptime(word, dateFormat).strftime(dateFormat)
					return word
				except ValueError:
					print("",end="")
		return self.findDateWithSpecialFormat(str)


	#retrun a string representrions of a date looks like this "פברואר 2001"
	def findDateWithSpecialFormat(self, str):
		str = re.sub(",", " ", str)
		words = str.split()
		index = 0
		date = ""
		for word in words:
			try:
				date = datetime.strptime(word, "%B").strftime("%B")
				if(index > 0):
					return words[index - 1] + " " + word + " " + words[index + 1]
			except ValueError:
				print("",end="")
			for hDate in self.m_HebrewMothsList:
				if ((word in hDate) or  (hDate in word)):
					try:
						date = datetime.strptime(words[index + 1], "%Y").strftime("%Y")
						if(index > 0):
							if(WordProsessor.hasNumbers(words[index - 1])):
								return  words[index - 1] + " " + word + " " + words[index + 1]
						return  word + " " + words[index + 1]
					except ValueError:
						print("",end="")
			index = index + 1
		if date in "":
			lines = lines = str.splitlines()
			for line in lines:
				for da in self.m_specialDates:
					if da in line:
						if da == "juillet 1911":
							da = "3 juillet 1911"
						date = da
		return date
