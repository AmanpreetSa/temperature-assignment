temperatures = [
  [-5.2,	-6,	-6,	-6.5,	-4,	-2.5,	0,	2,	3.4,	7,	12.2,	15.7,	18.4,	21.1,	21.2,	21.1,	18.4,	17.2,	12.3,	9.4,	7.7,	2.4,	0, -2.7],
  [-3.8,	-5.9,	-5.8,	-4.9,	-3.1,	-1.4,	0.8,	2.8,	4.7,	8.4,	12.5,	16.8,	18.8,	21.7,	22.5,	22.8,	18.8,	18.3,	12.4,	10.7,	7.8,	4.3,	0.3,	-0.7],
[-2.4,	-4.8,	-5.0,	-3.0,	-2.0,	0.1,	2.0,	3.6,	6.1,	9.4,	13.0,	18.7,	19.7,	22.2,	23.3,	24.7,	19.0,	19.0,	12.7,	11.0,	9.7,	6.1,	2.3,	0.0]
]

for day in temperatures:
  totalTemp = 0 
  for hours in day:
    totalTemp += hours
  totalAverage = round(totalTemp / len(day), 1)
  print(f"The average daily temperature was " + str(totalAverage) + "°C")
