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
	def writeLines(self, lines):
		with open(self.m_fileName, 'a') as csvFile: 
			writer = csv.DictWriter(csvFile, fieldnames=self.m_fieldNames)
			for line in lines:
				writer.writerow(line)

				
x = CSVHandler("test.csv", ["name", "age"])
x.writeLines([{"name" : "gena", "age" : 26}, {"name" : "reut", "age" : 27}])
x.writeLines([{"name" : "gena12", "age" : 26}, {"name" : "reut1", "age" : 27}])
			
		
'''
with open("test.csv", 'w') as csvFile:
	fieldnames = ['first_name', 'last_name']
	writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
	
	writer.writeheader()
	writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
	writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
	writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
	'''