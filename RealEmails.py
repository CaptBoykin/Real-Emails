#!/usr/bin/python

import re

#What's really on your mind? Each word is replaced by the corresponding string
#For example, hope will get replaced with:"genuinely do not care if"
fixit = {
	'hope':'genuinely do not care if',
	'did you':'did you fucking',
	'Per my last email,':'Did you fucking read my last email',
	'take your time':'please, can you hurry the fuck up',
	'I\'m not in a rush':'We are literally waiting on you',
	'Respectfully':'Take a long walk off a short pier',
	'not up to standards':'an ass sandwich',
	'sub par':'butt fudge',
	'Sincerely':'Choke on my balls',
	'sounds good':'sounds god awful',
	'I can\'t wait!':'I\'d rather nail my dick to a table',
	'no rush':'hurry the fuck up',
	'pushing to the right':'delaying forever',
	'pushed to the right':'delayed forever',
	'meeting':'torture-fest'
}
def replfunc(match):
   return fixit[match.group(0)]

#Slaps everything together for sendin'
#Where email.txt is your original file and email-fix.txt will be created
regex = re.compile('|'.join(re.escape(x) for x in fixit))
with open('email.txt') as fin, open('email-fixed.txt','w') as fout:
    for line in fin:
        fout.write(regex.sub(replfunc,line))
