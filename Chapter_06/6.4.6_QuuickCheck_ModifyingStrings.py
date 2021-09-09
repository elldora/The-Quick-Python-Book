'''QUICK CHECK: MODIFYING STRINGS 
What would be a quick way to change all
punctuation in a string to spaces?'''

import re
import string
#first
my_str = "hey##@there@ &*)?6"
specialChars = "!@#$%^&*()[]{};:,./<>?\|`~-=_+\""
replacements = "                               " #corresponding characters in inCharSet to be replaced
tabel = my_str.maketrans(specialChars, replacements)
result_str = my_str.translate(tabel)
print(result_str)
# second
my_str = "hey$there~!6"
my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', ' ', my_str)
print (my_new_string)

# third
chars = re.escape(string.punctuation)
print (re.sub(r'['+chars+']', ' ',my_str))