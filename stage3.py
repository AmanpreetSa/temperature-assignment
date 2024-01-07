#create a new list for temperatures and open the file to gain access, add that information to a variable called file
temperatures = []
file = open("temperature.csv")
#goes through each line in the csv file 
for line in file:
  currentDay = []
  #splits the line by the commas and then loops through each hour to find it 
  for hour in line.split(","):
    #checks to see if there is an empty space, if so then adds 'None'
    if hour == "":
      currentDay.append(None)
    #else if there is a number/temp there then convert to float since it was a string, and adds it to the current day
    else:
      currentDay.append(float(hour))
#adds the current day to the list of temperatures
  temperatures.append(currentDay)

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
