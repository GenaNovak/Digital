from Parser 	   import Parser
from WordProsessor import WordProsessor
from CSVHandler    import CSVHandler
from Letter        import Letter
import glob

def create_csv(dir_path):
    letters = []
    prosessor = WordProsessor()
    for file in glob.glob("out/*.txt"):
    	letters.append(Letter(prosessor.getText(file), file))

    x = CSVHandler("test.csv", ["Date", "To", "From",  "Number of words", "Number of words(with stop words)"])
    x.writeLines(letters)

def main():
	input_dir_path  = 'input'
	output_dir_path = 'out'
	#Parser.splite_to_letters(input_dir_path, output_dir_path)
	create_csv(output_dir_path);


main()
