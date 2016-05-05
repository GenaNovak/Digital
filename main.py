from Parser 	   import Parser
from WordProsessor import WordProsessor
from CSVHandler    import CSVHandler
from Letter        import Letter
import glob
import fnmatch
import os


def createCsv(dir_path):
    letters = []
    prosessor = WordProsessor()
    for root, dirnames, filenames in os.walk('./out'):
        for filename in fnmatch.filter(filenames, '*.txt'):
            file = os.path.abspath(os.path.join(root, filename))
            letters.append(Letter(prosessor.getText(file),file))

    x = CSVHandler("out/output.csv", ["Date", "adressee", "From", "Location", "Number of words", "Number of words(with stop words)", "filename"])
    x.writeLines(letters)

def parseTaggerOutput(lettersNames, p):
    for name in lettersNames:
        words = p.parseTaggerOutput(name)
        lname = name.split("_")[0]
        p.writeTaggerData(WordProsessor().countWords(words), "./out", lname)

def main():
    input_dir_path = "input"
    output_dir_path = "out"
    p = Parser()
    p.parseFolder(input_dir_path, output_dir_path)
    createCsv(output_dir_path)
    parseTaggerOutput(["rivka_letters.txt","sara_letters.txt"], p)

main()
