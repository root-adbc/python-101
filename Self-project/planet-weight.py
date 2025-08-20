# create a weight conversaion program

earth_weight = float(input("What is your Earth weight?:" + ""))
planet_num = int(input("Planet number?:"+""))


# destination weight = earth weight x relative gravity

# calculate users weight 
# If user enters a planet number outisde of 1-7, print a message saying "Invalid planet number"

# to calculate user weight on Mars:
# destination_weight = earth_weight * 0.38

# planet number variable

#mercury = 1
#venus = 2
#mars = 3
#jupiter = 4
#saturn = 5
#uranus = 6
#neptune = 7

# planet Relative Gravity variable
#mercury_rg = 0.3
#venus_rg = 0.91
#mars_rg = 0.38
#jupiter_rg = 2.53
#saturn_rg = 1.07
#uranus_rg = 0.89
#neptune_rg = 1.14


# to calculate user weight on Mars:
# destination_weight = earth_weight * 0.38

if planet_num ==1:
  destination_weight = earth_weight * 0.38
elif planet_num == 2:
  destination_weight = earth_weight * 0.91
  print(destination_weight)
elif planet_num == 3:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif planet_num == 4:
  destination_weight = earth_weight * 2.53
  print(destination_weight)
elif planet_num == 5:
  destination_weight = earth_weight * 1.07
  print(destination_weight)
elif planet_num == 6:
  destination_weight = earth_weight * 0.89
  print(destination_weight)
elif planet_num == 7:
  destination_weight = earth_weight * 1.14
  print(destination_weight)
else:
  print("Invalid planet number")
