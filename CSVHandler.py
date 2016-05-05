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
				row = {"Date" : letter.m_date.m_dateStr, "adressee" : letter.m_to, "From" : letter.m_from, "Location" : letter.m_location, "Number of words" : letter.m_numberOfWords, "Number of words(with stop words)" : letter.m_numberOfWordsWithoutStopWords, "filename" : letter.m_letterPath}
				writer.writerow(row)
