import re # importing regular expression

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp'] #raw script

#contains the letter e
for elements in accessions:
    result1 = re.match(r"(e\w+)", accessions)

if result1:
    print((result1.groups))
#contain the letters d and e in that order
for elements in accessions:
    result2 = re.match(r"(de\w+)", accessions)

if result2:
    print((result2.groups))
#contain the number 5
for element in accessions:

    result9 = re.match(r'(5\d)', accessions)
    if result9:
        print(result9.groups)
#contain the letters d and e in that order with a single letter between them
for elements in accessions:
    result3 = re.match(r"(d.e\w+)", accessions)

if result1:
    print((result1.groups))
# Find all words starting with d or p.
for element in accessions:

    result4 = re.match("^d|p\w", accessions)
    if result4:
        print("START:", element)

#start with x or y
for element in accessions:

    result5 = re.match("^x|y\w", accessions)
    if element == result5:
        print("START:", accessions)

#start with x or y and end with e
for element in accessions:

    result6 = re.match("^x|y\w", accessions)
    if result6:
        print (result6.groups)
#contain three or more digits in a row
for element in accessions:

    result7 = re.match(r"/d/d/d/", accessions)
    if result7:
        print(result7.groups)
#end with d followed by either a, r or p
for element in accessions:

    result8 = re.match(r"$da|r|p\w", accessions)
    if result8:
        print(result8.groups)

