# -*- coding: utf-8 -*-
import os, glob, re

class Parser:
        def __init__(self):
                self.m_inletter_seperat= {
                        5  : ['שלום רב לגבירות','שלום לכן יקירותי','לכבוד העלמות הנכבדות'],
                        32 : 'P.A.',                     #rivka 1912 --> letter 2
                        36 : 'רבקה!',                    #rivka 1912 --> letter 6
                        61 : ['הנייר היפה','המכתב נשאר'], #rivka 1913 --> letter 6
                        63 : 'האם',                      #rivka 1913 --> letter 8
                        64 : 'P.S.',                     #rivka 1913 --> letter 9
                        66 : "שרה'לה נשמתי",           #rivka 1914 --> letter 1
                        73 : 'לשרה שלום'                #rivka 1914 --> letter 8
                        }

        def getAbsPath(self, rel_path):
                script_path = os.path.abspath(__file__)
                script_dir = os.path.split(script_path)[0]
                abs_file_path = os.path.join(script_dir, rel_path)
                return abs_file_path


        def removeEmptyLine(self, text):
                newlines = []
                lines = text.splitlines()
                for line in lines:
                        line = line.strip()
                        if line not in "":
                                newlines.append(line)
                return "\n".join(newlines)

        def cleanLetterText(self, text):
                #remove specific pattern so it will be convinant to split
                uniform_regex = '(<!\[if !supportEmptyParas\]>[\s]*<!\[endif\]>[\s\n\r\t]*)*\* \* \*[\s\n]*(<!\[if !supportEmptyParas\]>[\s]*<!\[endif\]>[\s\n\r\t]*)*'
                text = re.sub(uniform_regex,'\n * * * \n',text);

                #add delimiter to split into letters
                pattern_beforeyear = '<!\[if !supportEmptyParas\]>[\s]*<!\[endif\]>[\s\n\r\t]*';
                sperat_years = ['1912', '1913', '1914', '1915', '1917']
                for year in sperat_years:
                    pattern = pattern_beforeyear + year
                    repl = '\n * * * \n {0}'.format(year)
                    text = re.sub(pattern, repl, text)
                
                boarder_str = 'לתוכן הענינים'
                sidx = text.find(boarder_str)                          
                sidx_plus = text.find(boarder_str) + len(boarder_str)  #sidx_plus = start of the text
                eidx = text.find(boarder_str,sidx_plus)                #eidx = end of the text     
                if (sidx == -1):
                        print("could not trim start")
                        sidx_plus = 0
                if (eidx == -1):
                        print("could not trim end")
                        eidx = len(text)

                # clean special marks
                text = re.sub(r'<.*?>' ,'', text)
                text = re.sub(r'\[[0-9].*?\]', '', text)
                text = re.sub(",", " , ", text)
                text = re.sub("-", " - ",text)
                text = self.removeEmptyLine(text)
                
                return text[sidx_plus:(eidx-1)]

        def writeLetter(self, path, letter, count):
                fname = 'letter_{0}.txt'.format(count)
                out_file_path = os.path.join(path, fname)
                with open(out_file_path, 'wb') as out_file:
                        out_file.write(letter.encode())
                print("    write to {0}".format(fname))
                return count+1

        def spliteInLetter(self, out_dir_path, text, val, lcount, pcount):    
                if (isinstance(val, str)):
                        repl = '\n * * * \n {0}'.format(val)
                        text = re.sub(val, repl, text)
                else:
                        for v in val:
                                repl = '\n * * * \n {0}'.format(v)
                                text = re.sub(v, repl, text)
                letters = text.split('* * *')   
                for letter in letters:
                        pcount = self.writeLetter(out_dir_path,letter,pcount)
                return pcount

        def parseFolder(self, in_dir_path, out_dir_path):
            
                if (not (os.path.exists(in_dir_path))):
                        print('Input folder doesn''t exist')
                        return

                #read all files in input directory
                os.chdir(in_dir_path)
                for file in glob.glob("*.txt"):
                        # open file for read
                        in_abs_path = self.getAbsPath(os.path.join(in_dir_path, file))
                        with open(in_abs_path, 'rb') as input_file:
                                all_text = input_file.read().decode()
                        all_text = self.cleanLetterText(all_text)
                        
                        out_path = os.path.join(out_dir_path, os.path.splitext(file)[0])
                        out_abs_path = self.getAbsPath(out_path)
                        #create out dir if it doesn't exist
                        os.makedirs(out_abs_path, exist_ok=True)

                        # ------ Parse with tagger -----------



                        # ------ Split into letters ----------
                        
                        print(os.path.basename(out_abs_path))
                        all_letters = all_text.split('* * *')
                        letter_count = 1;
                        print_count = 1;
                        for letter in all_letters:
                                if letter_count in self.m_inletter_seperat:
                                        val = self.m_inletter_seperat.get(letter_count)
                                        print_count = self.spliteInLetter(out_abs_path, letter, val, letter_count, print_count)
                                else:
                                        print_count = self.writeLetter(out_abs_path, letter, print_count)
                                letter_count = letter_count + 1
                os.chdir("..")
