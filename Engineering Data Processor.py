'''
Exercise 1: Engineering Data Processor (Reinforcement)
Write a program that processes electrical measurement data:
measurements = [220.5, 225.2, 218.9, 230.1, 215.6, 228.3, 222.7]
Your program should:

Use a while loop to find the first voltage reading above 225V
Use a for loop to calculate the average voltage
Use conditional logic to count how many readings are within ±5% of 220V
Print all results with proper labels

This reinforces: loops, conditionals, variables, basic math operations
'''


measurements = [220.5, 225.2, 218.9, 230.1, 215.6, 228.3, 222.7]

#Find the first voltage that higher than 225V
i = 0
while i < len(measurements) and measurements[i] <= 225:  #Boundary check not to pick data more than list
    i = i + 1

if i < len(measurements):   #Boundary check if there is no > 225V
    Above225V = measurements[i]
    print('The first voltage more than 225 is:', Above225V)
else:
    print('No higher than 225V')

#Find the average power in the list
TotalVoltage = 0
count = 0
for Voltage in measurements:
    TotalVoltage = TotalVoltage + Voltage
    count = count + 1

AverageVoltage = TotalVoltage / count
print('The Average Voltage is:', AverageVoltage)

#Count how many voltage readings are within +- 5% of 220V with conditional logic
Range_Voltage_Bottom = 220 * 0.95
Range_Voltage_Top = 220 * 1.05
Voltage_Count = 0

for Voltage in measurements:
    if Range_Voltage_Bottom <= Voltage <= Range_Voltage_Top:
        Voltage_Count = Voltage_Count + 1

print(Voltage_Count)
