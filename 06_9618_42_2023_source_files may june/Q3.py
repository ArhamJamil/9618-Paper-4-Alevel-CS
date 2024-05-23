class Employee:
    def __init__(self, hourlyPay, employeeNumber, jobTitle):
        self.__HourlyPay = hourlyPay
        self.__EmployeeNumber = employeeNumber
        self.__JobTitle = jobTitle
        self.__PayYear2022 = [0.0 for _ in range(0,52)]


    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    

    def SetPay(self, Wnum, Nhours):
        pay = float(self.__HourlyPay) * float(Nhours)
        self.__PayYear2022[int(Wnum)] = pay

    def GetTotalPay(self):
        Total = 0
        for index in range(0,len(self.__PayYear2022)):
            Total = Total + self.__PayYear2022[index]

        return Total
            

class Manager(Employee):
    def __init__(self, hourlyPay, employeeNumber, jobTitle, bonusVal):
        super().__init__(hourlyPay, employeeNumber, jobTitle)
        self.BonusValue = bonusVal

    def SetPay(self, Wnum, Nhours):
        bonusAmount = float(Nhours) * (self.BonusValue / 100)
        totalHours = float(Nhours) + bonusAmount
        super().SetPay(Wnum, totalHours)
    

global EmployeeArray

EmployeeArray = [Employee for _ in range(0,8)]
try:
    File = open("Employees.txt", "r")
    HourlyPay = ""
    EmployeeNumber = ""
    BonusValue = ""
    JobTitle = ""

    FileData = HourlyPay + EmployeeNumber + BonusValue + JobTitle
    print(FileData)

    index = 0

    for count in range(0,8):
        HourlyPay = File.readline().strip()
        EmployeeNumber = File.readline().strip()
        try:
            BonusValue = File.readline().strip()
            Bonus = float(BonusValue)
            JobTitle = File.readline().strip()
            manager = Manager(HourlyPay, EmployeeNumber, JobTitle, Bonus)
            EmployeeArray[count] = manager
            index = index + 1
        except:
            JobTitle = BonusValue
            employee = Employee(HourlyPay,EmployeeNumber,JobTitle)
            EmployeeArray[count] = employee
            index = index + 1
        
except:
    print("File Not Found")

def EnterHours():
        File = open("HoursWeek1.txt", "r")
        for lines in range(0, len(EmployeeArray)):
            employeeNum = File.readline().strip()
            NumOfHours = File.readline().strip()
            for index in range(0,len(EmployeeArray)):
                if EmployeeArray[index].GetEmployeeNumber() == employeeNum:
                    EmployeeArray[index].SetPay(Wnum=1, Nhours=NumOfHours)
                
EnterHours()
for employee in range(0,8):
    print(EmployeeArray[employee].GetEmployeeNumber(), " ", EmployeeArray[employee].GetTotalPay())
  
