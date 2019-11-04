import re # importing regular expression

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp'] #raw script

#contain the letter d or e
pattern = re.compile(r'd|e')
#contain the letters d and e in that order
pattern = re.compile(r'de')
# contain the number 5
pattern = re.findall(r'5')
#contain the letters d and e in that order with a single letter between them
pattern = re.compile(r'd|.|e')
#contain both the letters d and e in any order
pattern = re.findall(r'de')
#start with x or y
pattern = re.compile(r'x|y')
#start with x or y and end with e
pattern = re.compile(r'x|y$e')
#contain three or more digits in a row
pattern = re.compile(r'/d{3}.')
#end with d followed by either a, r or p
pattern = re.compile(r'd$a|r|p')
matches = pattern.finditer(str(accessions))


for match in matches:
    print(match)
