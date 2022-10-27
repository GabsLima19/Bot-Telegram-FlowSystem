def lersensores():
    while True:
        with open('dados.csv') as f:
            sensor = str(f.readlines())
            splitSen = sensor.split(';') 

        sensorA = []
        sensorB = []


        for i in range(len(splitSen)):
            #print(splitSen[i])
            split = splitSen[i].split(',')
            if len(split) != 1:
                sensorA.append(split[0])
                sensorB.append(split[1])

        return(sensorA[-1], sensorB[-1])
        