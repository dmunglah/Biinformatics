accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

print (accessions[1:8])

print (accessions[-1])

from operator import itemgetter  

print(*itemgetter(0, 4, 5, 6)(accessions))

print(accessions[4])

print (accessions[3:6], accessions[-1])

print(*itemgetter(0, 1, 5)(accessions))

print (accessions[-3])

print(*itemgetter(0, 3, 4)(accessions)) 

print(*itemgetter(-1,-2)(accessions)) 
