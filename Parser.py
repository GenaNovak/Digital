# -*- coding: utf-8 -*-
import os, glob, re

class Parser:
        def get_abs_path(rel_path):
                script_path = os.path.abspath(__file__)
                script_dir = os.path.split(script_path)[0]
                abs_file_path = os.path.join(script_dir, rel_path)
                return abs_file_path

        def clean_letter_text(text):
                #add delimiter to split into letters
                #text = text.replace('1917','\n * * * \n 1917')
                
                uniform_regex = '\* \* \*[\s\n]*?(<!\[if !supportEmptyParas\]>[\s]*<!\[endif\]>[\s\n\r\t]*)+';
                text = re.sub(uniform_regex,'* * * \n',text);

                pattern_beforeyear = '<!\[if !supportEmptyParas\]>[\s]*<!\[endif\]>[\s\n\r\t]*';
                sperat_years = ['1912', '1913', '1914', '1915', '1917']
                for year in sperat_years:
                    pattern = pattern_beforeyear + year
                    repl = '\n * * * \n {0}'.format(year)
                    print(pattern)
                    text = re.sub(pattern, repl, text)
                '''
                text = re.sub('1917','\n * * * \n 1917',text)
                tmp = '<![endif]>\n  1912'
                if (text.find(tmp) != -1):
                    print("found\n")
                else:
                    print("didnt found\n")
                '''
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

                return text[sidx_plus:(eidx-1)]

        def splite_to_letters(in_dir_path, out_dir_path):

                if (not (os.path.exists(in_dir_path))):
                        print('Input folder doesn''t exist')
                        return

                #read all files in input directory
                os.chdir(in_dir_path)
                for file in glob.glob("*.txt"):
                        # open file for readin
                        in_abs_path = Parser.get_abs_path(os.path.join(in_dir_path, file))
                        with open(in_abs_path, 'rb') as input_file:
                                all_text = input_file.read().decode()

                        all_text = Parser.clean_letter_text(all_text)
                        '''with open('c:\\ass1\\out.txt', 'wb') as out_file:
                                       out_file.write(all_text.encode())
                        '''
                        out_path = os.path.join(out_dir_path, os.path.splitext(file)[0])
                        out_abs_path = Parser.get_abs_path(out_path)
                        print(os.path.basename(out_abs_path))
                        #create out dir if it doesn't exist
                        os.makedirs(out_abs_path, exist_ok=True)
                        all_letters = all_text.split('* * *')
                        count = 1;
                        for letter in all_letters:
                                fname = 'letter_{0}.txt'.format(count)
                                out_file_path = os.path.join(out_abs_path, fname)
                                with open(out_file_path, 'wb') as out_file:
                                       out_file.write(letter.encode())
                                count = count+1
                                print("    write to {0}".format(fname))
                os.chdir("..")
