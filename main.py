from Parser 	   import Parser
from WordProsessor import WordProsessor
from CSVHandler    import CSVHandler
from Letter        import Letter
import glob
import fnmatch
import os


def create_csv(dir_path):
    letters = []
    prosessor = WordProsessor()
    '''for file in glob.glob("out/*.txt"):
    	letters.append(Letter(prosessor.getText(file), file))
    '''
    for root, dirnames, filenames in os.walk('./out'):
        for filename in fnmatch.filter(filenames, '*.txt'):
            file = os.path.abspath(os.path.join(root, filename))
            letters.append(Letter(prosessor.getText(file),file))

    x = CSVHandler("test.csv", ["Date", "To", "From", "Location", "Number of words", "Number of words(with stop words)", "Path"])
    x.writeLines(letters)


def main():
    input_dir_path = "input"
    output_dir_path = "out"
    p = Parser()
    p.spliteToLetters(input_dir_path, output_dir_path)
    create_csv(output_dir_path)

main()
