import csv

class CSVHandler:
	def __init__(self, fileName, fieldNamesArr):
		self.m_fileName = fileName
		self.m_fieldNames = fieldNamesArr
		self.m_didWriteHeaders = 0
		with open(self.m_fileName, 'w') as csvFile:
			writer = csv.DictWriter(csvFile, fieldnames=fieldNamesArr)
			writer.writeheader()


	#append the new row to the table
	def writeLines(self, letters):
		with open(self.m_fileName, 'a') as csvFile:
			writer = csv.DictWriter(csvFile, fieldnames=self.m_fieldNames)
			for letter in letters:
				row = {"Date" : letter.m_date.m_dateStr, "To" : letter.m_to, "From" : letter.m_from, "Location" : letter.m_location, "Number of words" : letter.m_numberOfWords, "Number of words(with stop words)" : letter.m_numberOfWordsWithoutStopWords, "Path" : letter.m_letterPath}
				writer.writerow(row)



'''
with open("test.csv", 'w') as csvFile:
	fieldnames = ['first_name', 'last_name']
	writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

	writer.writeheader()
	writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
	writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
	writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
	'''
