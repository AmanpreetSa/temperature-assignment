temperatures = [[-5.2,-6,-6,-6.5,-4,-2.5,0,2,3.4,7,12.2,15.7,18.4,21.1,21.2,21.1,18.4,17.2,12.3,9.4,7.7,2.4,0,-2.7], [-3.4,-5.8,None,-5.7,-3.7,-0.5,1.7,None,5.3,8.6,14.0,16.4,19.2,22.3,23.0,21.6,19.4,17.4,None,10.8,7.9,2.6,0.0,-2.0], [-3.3,None,None,None,None,0.9,2.3,4.0,5.6,10.1,None,None,None,None,None,None,None,18.8,14.3,11.8,8.2,3.7,0.8,0.0], [-2.4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,2.0]]

#the for loop goes through each list which is a seperate day
for day in temperatures:
  lastProperIndex = None 
  lastProperTemp = None
  improperData = None
  #this for loop now goes through each index, wihch is the hourly temperature in that day
  for i in range(len(day)): 
    hour = day[i]
    #this if statement checks if there is a temperature at the hour listed
    if hour == None:
      improperData = True
    #this else if statement checks to see if there any 'None' in the list to then find the average
    elif improperData == True:
      improperData = False
      avgHourlyTemp =  (hour + lastProperTemp) / 2
      #goes through all the values that are none and replaces them with all the new, appropriate temps
      for i2 in range(lastProperIndex + 1, i):
        day[i2] = avgHourlyTemp
    #saves the data since it is valid
    else:
      lastProperIndex = i
      lastProperTemp = hour  

  #these statements calculates the average temperature of each day, then prints it into the console
  totalTemp = 0 
  for hours in day:
    totalTemp += hours
  totalAverage = round(totalTemp / len(day), 1)
  print(f"The average daily temperature was " + str(totalAverage) + "°C")
