# # coding='utf8'
# import re

# # var = "{\"name\":\"lll\"},{\"name\":\"lly\"}"
# var = 'I\'m singing while you\'re'
# # str = "abcaxc"

# matcher = re.match('\b\\w+ing\b', var, re.M)

# # matcher = re.match('ab*c', str, re.M)

# print matcher.group(0)

import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"