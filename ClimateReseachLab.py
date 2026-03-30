import csv
import os

class Measurement():
    def __init__(self,dayNo,temp, humidity, HSI=0, RL="unknown"):
        self.dayNo = dayNo
        self.temp = temp
        self.humidity = humidity
        self.HSI = HSI
        self.RL = RL

    def calculateHSI(self):
        self.HSI = (0.7 * self.temp) + (0.2 * self.humidity)
        return self.HSI
    
    def classifyHSI(self):
        if self.HSI == 0:
            return "Please calculate the HSI, it is still default value"
        elif self.HSI < 40: 
            self.RL = "Safe"
        elif 40 <= self.HSI <= 59.9:
            self.RL = "Caution"
        elif 60<= self.HSI <= 79.9:
            self.RL = "Danger"
        elif self.HSI >= 80:
            self.RL = "Extreme"
        else:
            return "Unknown error"
        return self.RL


def getFromFile():
    filename = "HSI_Data.csv"
    #checking if it exists in file path
    if os.path.isfile(filename):
        with open("HSI_Data.csv", mode='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                print(line)
    else:
        print("Error it doesn't exist")

def putInfile(dataReadings):
    if dataReadings == [] :
        print("Error cannot add empty data readings")
        return 0
    else:
        filename = "HSI_Data.csv"
        #checking if it exists in file path
        if os.path.isfile(filename):
            print(f"The CSV file '{filename}' exists")
        else:
            print("It doesn't exist, setting it up now.")
            fields = ['Day Number','Temperature','Humidity','Heat Stress Index','Risk Level']
            #putting the data objects into arrays and then putting those arrays into an array
            rows = []
            for i in range(0,len(dataReadings)):
                curr_row = [dataReadings[i].dayNo,dataReadings[i].temp,dataReadings[i].humidity,dataReadings[i].HSI,dataReadings[i].RL]
                rows.append(curr_row)
            #data is prepped and now ready for data insertion into the csv
            with open(filename,'w',newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
                csvwriter.writerows(rows)
        return 1


def calculateAverage(dataReadings):
    if dataReadings == []:
        print("Error dataReadings is empty please enter values.")
        return 0
    else:
        total = 0 
        for i in range(0,len(dataReadings)):
            total += dataReadings[i].HSI
        avg = total / len(dataReadings)
        return avg

def getHighest(dataReadings):
    maxTemp = -999
    maxDay = -0
    for i in range(len(dataReadings)):
        if dataReadings[i].temp > maxTemp:
            maxTemp = dataReadings[i].temp
            maxDay = dataReadings[i].dayNo
    return f"Highest Temperature was {maxTemp} on day {maxDay}"

def countExtreme(dataReadings):
    if dataReadings == []:
        print("Error dataReadings is empty please enter values.")
        return 0
    else:
        count = 0
        for i in range(len(dataReadings)):
            if dataReadings[i].RL == "Extreme":
                count +=1 
        return f"Count of extreme Risk levels : {count}"
dataReadings = []
def main():
    choice = 0
    while choice != 4:
        print("="*100)
        print("\t \t \t \t \t Welcome to the HSI System ")
        print("\t \t \t \t Press the corresponding number to navigate ")
        print("\t \t \t \t 1. Data entry ")
        print("\t \t \t \t 2. Data Viewing ")
        print("\t \t \t \t 3. E.D.A ")
        print("\t \t \t \t 4. Exit ")
        choice = int(input("\t \t \t \t \t Enter choice: "))
        if choice == 1: 
            days = -1
            while days < 0:
                try:
                    days = int(input("\t \t \t Enter the number of days to enter : "))
                    if days < 0 :
                        raise ValueError
                except ValueError:
                    print("\t \t \t Invalid input, please re-enter a non-negative number (digit) for the day.")
            for day in range(days):
                tempValid =  False
                while tempValid == False:
                    try:
                        temp = float(input(f"\t \t \t Enter the temperature for day no. {day+1} :"))
                    except ValueError:
                        print("\t \t \t Error! Wrong data type")
                    else:
                        tempValid = True #will leave the loop
                humidity = -1
                while humidity < 0 or humidity > 100: #we assume the user hasn't entered a valid one yet
                        try:
                            humidity = float(input(f"\t \t \t Enter the humidity for day no. {day+1} :"))
                            if humidity < 0 or humidity > 100:
                                raise ValueError
                        except ValueError:
                            print("\t \t \t Error, out of range should be between 0 and 100 inclusive")
                measurements = Measurement(day+1,temp,humidity)
                measurements.calculateHSI()
                measurements.classifyHSI()
                dataReadings.append(measurements)
            putInfile(dataReadings)
        elif choice == 2:
            getFromFile()
        elif choice == 3:
            avg = calculateAverage(dataReadings)
            print(avg)
        elif choice == 4:
            print("\t \t \t  Exitting")
        else:
            print("\t \t \t  Invalid input.")
        
if __name__ == "__main__":
    main()