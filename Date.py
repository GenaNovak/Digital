from datetime import datetime
from WordProsessor import WordProsessor
import re

class Date:
	def __init__(self, str):
		self.m_supportedDateFormats = ["%d.%m.%Y", "%d.%m.%y", "%Y %B"]
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
					return date
				except ValueError:
					print("",end="")
		return self.findDateWithSpecialFormat(str)


	#retrun a string representrions of a date looks like this "פברואר 2001"
	def findDateWithSpecialFormat(self, str):
		str = re.sub(",", " , ", str)
		words = str.split()
		index = 0
		date = ""
		for word in words:
			for hDate in self.m_HebrewMothsList:
				if ((word in hDate) or  (hDate in word)):
					try:
						date = datetime.strptime(words[index + 1], "%Y").strftime("%Y")
						return  word + " " + date
					except ValueError:
						print("",end="")
			index = index + 1
		return date
