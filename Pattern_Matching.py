import re 

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

pattern = re.compile(r'd')
pattern = re.compile(r'e')
pattern = re.compile(r'de')
pattern = re.compile(r'5')
pattern = re.compile(r'5')
pattern = re.compile(r'd'), re.compile(r'e')
pattern = re.compile(r'xy')
pattern = re.compile('\d{0,3}')
pattern = re.compile(r'd,a,r,p')
pattern = re.compile(r'xye')

matches = pattern.finditer(str(accessions))

for match in matches:
    print(match)
    
    
