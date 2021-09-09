import os
import re

file_name = "moby_01.txt"
file_name2 = "moby_01_clean.txt"
dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + file_name
dir_path2 = os.path.dirname(os.path.realpath(__file__)) + '\\' + file_name2
#print(dir_path)
with open(dir_path) as infile, open(dir_path2, "w") as outfile:
    for line in infile:
        cleaned_words = ""
        print(cleaned_words)
        lower_cased = line.lower()
        print(lower_cased)
        removed_punc = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lower_cased)
        print(removed_punc)
        cleaned_words = removed_punc.split()
        print(cleaned_words)
        # make all one case
        # remove punctuation
        # split into words
        # write all words for line
        for i in range(len(cleaned_words)):
            outfile.write(cleaned_words[i]+"\n")




#for f in os.listdir():
#	print(f)