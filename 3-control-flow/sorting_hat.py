# The Sorting Hat project 

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print ("   1) Dawn")
print ("   2) Dusk")

Q1 = int(input(" Enter answer (1,2)"))

if Q1 == 1:
  Gryffindor = Gryffindor +1
  Ravenclaw = Ravenclaw +1
elif Q1 == 2:
  Hufflepuff = +1
  Slytherin = +1
else:
  print("Wrong input")

#print(Gryffindor)
#print(Ravenclaw)
#print(Huffleclaw)
#print(Slytherin)
######
print("==================================")

print ("Q2) When I’m dead, I want people to remember me as:")
print (     "1) The Good")
print (     "2) The Great")
print (     "3) The Wise")
print (     "4) The Bold")
print("==================================")
Q2 = int(input(" Enter answer (1,2,3 and 4)"))

if Q2 ==1:
  Hufflepuff=Hufflepuff +2
elif Q2 ==2:
  Slytherin = Slytherin +2
elif Q2 ==3:
  Ravenclaw = Ravenclaw +2
elif Q2 ==4:
  Gryffindor = Gryffindor +2
else:
  print("Wrong input")

########
print("Q3) Which kind of instrument most pleases your ear?")
print (    "1) The violin")
print (    "2) The trumpet")
print (    "3) The piano")
print (    "4) The drum")
print("==================================")

Q3 = int(input("Enter answer (1,2,3 and 4)"))

if Q3 ==1:
  Slytherin = Slytherin +4
elif Q3 ==2:
  Hufflepuff = Hufflepuff +4
elif Q3 ==3:
  Ravenclaw = Ravenclaw +4
elif Q3 ==4:
  Gryffindor = Gryffindor +4
else:
  print ("Wrong input")

# Print out the score for each house
print("Slytherin:"+ str(Slytherin))
print("Hufflepuff:" + str(Hufflepuff))
print("Ravenclaw:" + str(Ravenclaw))
print("Gryffindor:" + str(Gryffindor))
print("==================================")

# Figure out how to print out the house with the most points!

if Slytherin >= Hufflepuff and Slytherin >= Gryffindor and Slytherin >= Ravenclaw:
  print ("Slytherin! , the House with the most point")
elif Hufflepuff >= Gryffindor and Hufflepuff >= Ravenclaw and Hufflepuff>=Slytherin:
  print ("Hufflepuff! ,the House with the most point")
elif Gryffindor >= Ravenclaw and Gryffindor >= Slytherin and Gryffindor>= Hufflepuff:
  print("Gryffindor!, the House with the most point")

else:
  print ("Ravenclaw!,  the House with the most point")








