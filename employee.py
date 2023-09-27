"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    __onSalary = False
    __monthlySalary = 0
    __hoursWorked = 0
    __hourlySalary = 0
    __commissionType = ["none"]


    __bonus = 0
    __contractsLanded = 0
    __commissionPerContract = 0


    def __init__(self, name, onSalary, commission):
        self.__onSalary = onSalary
        self.name = name
        self.__commissionType = commission

    def setMonthlySalary(self, monthlySalary):
        self.__monthlySalary = monthlySalary

    def setHoursWorked(self, hoursWorked):
        self.__hoursWorked = hoursWorked

    def setHourlySalary(self, hourlySalary):
        self.__hourlySalary = hourlySalary

    def setContractsLanded(self, contractsLanded):
        self.__contractsLanded = contractsLanded

    def setCommissionPerContract(self, commissionPerContract):
        self.__commissionPerContract = commissionPerContract

    def setBonusCommision(self, bonus):
        self.__bonus = bonus


    def get_pay(self):

        if self.__onSalary == True:

            if self.__commissionType == "bonus":
                return self.__monthlySalary + self.__bonus
            elif self.__commissionType == "contract":
                return self.__monthlySalary + (self.__contractsLanded * self.__commissionPerContract)
            else:
                return self.__monthlySalary

        else:

            if self.__commissionType == "bonus":
                return (self.__hoursWorked * self.__hourlySalary) + self.__bonus
            elif self.__commissionType == "contract":
                return (self.__hoursWorked * self.__hourlySalary) + (self.__contractsLanded * self.__commissionPerContract)
            else:
                return self.__hoursWorked * self.__hourlySalary


    def __str__(self):

        workString = self.name + " works on a "
        if self.__onSalary == True:
            workString += "monthly salary of " + str(self.__monthlySalary)
        else:
            workString += "contract of " + str(self.__hoursWorked) + " hours at " + str(self.__hourlySalary) + "/hour"


        if self.__commissionType == "bonus":
            workString += " and receives a bonus commission of " + str(self.__bonus)
        elif self.__commissionType == "contract":
            workString += " and receives a commission for " + str(self.__contractsLanded) + " contract(s) at " + str(self.__commissionPerContract) + "/contract"


        workString += ". Their total pay is " + str(self.get_pay()) + "."



        return workString


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, "none")
billie.setMonthlySalary(4000)
print(billie.get_pay())
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, "none")
charlie.setHoursWorked(100)
charlie.setHourlySalary(25)
print(charlie.get_pay())
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, "contract")
renee.setMonthlySalary(3000)
renee.setContractsLanded(4)
renee.setCommissionPerContract(200)
print(renee.get_pay())
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, "contract")
jan.setHoursWorked(150)
jan.setHourlySalary(25)
jan.setContractsLanded(3)
jan.setCommissionPerContract(220)
print(jan.get_pay())
print(str(jan))


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, "bonus")
robbie.setMonthlySalary(2000)
robbie.setBonusCommision(1500)
print(robbie.get_pay())
print(str(robbie))


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, "bonus")
ariel.setHoursWorked(120)
ariel.setHourlySalary(30)
ariel.setBonusCommision(600)
print(ariel.get_pay())
print(str(ariel))


