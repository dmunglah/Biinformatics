# A list with different types 
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Manipulation of list
areas[-1] = 10.50
areas[4] = "chill zone"

#subset calculations
print(areas[3]+areas[-1])

#slicing 
downstairs = areas[0:6]
upstairs = areas[6:10
print(downstairs)
print(upstairs)               

#Extending list 
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)
                                  
#deleting 
del(areas[-4:-2])
                 
                     
