sensor = "0.1,0.22;13.5,6.5;5.40,3.6;"

splitSen = sensor.split(';') 

sensorA = [];
sensorB = [];


for i in range(len(splitSen)):
    ##print(splitSen[i])
    split = splitSen[i].split(',')
    if len(split) != 1:
        sensorA.append(split[0])
        sensorB.append(split[1])



print(sensorA)
print(sensorB)
