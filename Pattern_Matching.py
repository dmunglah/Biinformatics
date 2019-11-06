import re # importing regular expression

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp'] #raw script

#contains the letter d or e
for elements in accessions:
    result1 = re.match(r"(e\w+)", accessions)

if result1:
    print((result1.groups))
#contain the letters d and e in that order
result2 = re.match(r"\wde", accessions)
#contain the number 5
for element in accessions:
    result3 = re.match(r"\W5", accessions)

    # See if string starts in digit.
    m = re.match("5\d", element)
    if m:
        print("The elemetn that contains a number is :", element)
#contain the letters d and e in that order with a single letter between them
for elements in accessions:
    result1 = re.match(r"(d.e\w+)", accessions)

if result1:
    print((result1.groups))
# Find all words starting with d or p.
for element in accessions:

    # See if string starts in digit.
    m = re.match("^d|p\w", element)
    if m:
        print("START:", element)

    # See if string ends in digit.
    m = re.match("\wd|p$", element)
    if m:
        print("  END:", element)

#start with x or y
for element in accessions:

    # See if string starts in digit.
    m = re.match("^x|y\w", element)
    if m:
        print("START:", element)

#start with x or y and end with e
for element in accessions:

    # See if string starts in digit.
    m = re.match("^x|y\w", element)
    if m:
        print("START:", element)

    # See if string ends in digit.
    m = re.match("\we$", element)
    if m:
        print("  END:", element)
#contain three or more digits in a row
result8 = re.match(r".", accessions)
#end with d followed by either a, r or p
result9 = re.match(r".*", accessions)
