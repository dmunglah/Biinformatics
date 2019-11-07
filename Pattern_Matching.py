import re # importing regular expression

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp'] #raw script

#contains the letter e
for element in accessions:

    match = re.search(r'\w+', 'e')
    if match:
        print(match.group, accessions)
#contain the letters d and e in that order
for elements in accessions:
    result2 = re.match(r"(\Bde\w+)", accessions)

if result2:
    print(result2.group)
#contain the number 5
for element in accessions:

    match = re.search(r'\d', '5')
    if match:
        print(match.groups, element)
        
#contain the letters d and e in that order with a single letter between them
for element in accessions:

    match = re.search(r'd.e', 'de')
    if match:
        print(match.groups, element)

#start with x or y
for elements in accessions:
    result5 = re.match(r"(^x|y\w)", accessions)
    
    if result5:
        print("START:", result5.groups)

#start with x or y and end with e
for elements in accessions:

    result6 = re.match(r"(^x|y\w)", accessions)
    if result6:
        print (result6.groups)
#contain three or more digits in a row
for elements in accessions:

    result7 = re.match(r"(/d/d/d/)", accessions)
    if result7:
        print(result7.groups)
#end with d followed by either a, r or p
for elements in accessions:

    result8 = re.match(r"($da|r|p\w)", accessions)
    if result8:
        print(result8.groups)

