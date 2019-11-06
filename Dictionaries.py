####
#my_dict = {
   #"key1":"value1",
   #"key2":"value2",
#}

world = {"afganistan":30.55,
         "albania":2.77,
         "algeria":39.21}
world = []
world.apppend (argentina:44.27)
print(world)
sum(world.values())

# looping to find countries beginning with 'al' 
for element in world:
    # Match if starting with letter al.
    m = re.match("(al\w+)", element)

    # See if success.
    if m:
        print(m.groups())          
         
# adding a key to europe dictionary 
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe['italy'] = 'rome'
print(europe)

#deleting
del(europe['spain'])

print(europe['france']['capital'])

# Creating sub-dictionary data
data = { 'capital':'rome', 'population':59.83 }
europe['italy'] = data
print(europe)
