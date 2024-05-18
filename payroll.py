class Employee:
  def __init__(self, empid, empname, ssn,income = None):
    self.__empid = empid
    self.__empname = empname
    self.__ssn = ssn

  def get_empid(self):
    return self.__empid

  def get_empname(self):
    return self.__empname

  def get_ssn(self):
    return self.__ssn

  def get_income(self):
    return self.income

  def set_empname(self, newname):
    self.__empname = newname

  def calculate_income(self):
    pass

  def __repr__(self):
    return f"Employee ID: {self.__empid}\nEmployee name: {self.__empname}\nSocial Security Number: {self.__ssn}\nIncome: {self.income}"


class SalariedEmployee(Employee):
  def __init__(self, empid, empname, ssn):
    super().__init__(empid, empname, ssn)
    self.__ta = 600
    self.__da = 1000
    self.__hra = 1000

  def get_ta(self):
    return self.__ta

  def get_hra(self):
    return self.__hra

  def get_da(self):
    return self.__da

  def set_ta(self,new_ta):
    self.__ta = new_ta

  def set_da(self,new_da):
    self.__da = new_da

  def set_hra(self,new_hra):
    self.__hra = new_hra

  def calculate_income(self):
     basic = int(input("Enter the basic salary: "))
     self.income = basic+self.__ta+self.__da+self.__hra
     return self.income

class Management:
  emp_id_list = []
  emp_records = []

  def existing_employee(self,emp_id):
    for i in Management.emp_id_list:
      if i == emp_id:
        print("This employee ID already exists")
        return 0
    Management.emp_id_list.append(emp_id)
    return 1

  @classmethod
  def add_records(cls, employee):
    emp = {}
    emp["Id"] = employee.get_empid()
    emp["Name"] = employee.get_empname()
    emp["SSN"] = employee.get_ssn()
    emp["Salary"] = employee.get_income()
    Management.emp_records.append(emp)

  @classmethod
  def display_records(cls):
    for i in Management.emp_records:
      for j in i:
        print(f"{j} : {i[j]}")
      print("---------------------------------------")
    print("***************************************")


# Create an infinite while loop.
while True:
  id = input("Enter employee ID: ")
  manage = Management()

  while manage.existing_employee(id) == 0:
    print("Please enter a new employee id ")
    id = input("Enter employee ID: ")
  name = input("Enter employee name: ")
  ssn = input("Enter social security number: ")

  emp1 = SalariedEmployee(id, name, ssn)

  while True:
    print(f"\nTravelling allowance is {emp1.get_ta()}\nDearness allowance is {emp1.get_da()}\nHouse Rent allowance is {emp1.get_hra()}\n")
    print("-----Enter your choice------")
    user_choice = input("Enter 1 for updating Travelling allowance(TA)\nEnter 2 for updating Dearness allowance(DA)\nEnter 3 for updating House Rent allowance(HRA)\nEnter 4 to skip updating: ")
    while user_choice not in ['1','2','3','4']:
      print("-----Please enter a valid option------")
      user_choice = input("Enter 1 for updating Travelling allowance(TA)\nEnter 2 for updating Dearness allowance(DA)\nEnter 3 for updating House Rent allowance(HRA)\nEnter 4 to skip updating: ")

    if user_choice == '1':
      new_ta = int(input("\nEnter the new Travelling Allowance: "))
      emp1.set_ta(new_ta)
      print(f"Travelling allowance is {emp1.get_ta()}\n")
    elif user_choice == '2':
      new_da = int(input("Enter the new Dearness Allowance: "))
      emp1.set_da(new_da)
      print(f"Dearness allowance is {emp1.get_da()}\n")
    elif user_choice == '3':
      new_hra = int(input("Enter the new House Rent Allowance: "))
      emp1.set_hra(new_hra)
      print(f"House Rent allowance is {emp1.get_hra()}\n")
    else:
      break
    print("----------------------------------------")

    choice = int(input("Do you wish to continue updating TA, DA or HRA?\nEnter 1 for YES\nEnter 2 for NO\n"))

    if choice == 2:
      break


  print(f"\n--------Calculating Income----------------")
  emp1.calculate_income()
  print("\n--------Employee Details----------------")
  print(emp1)
  print("\n----------------------------------------")
  Management.add_records(emp1)
  choice_display=int(input("\nView All Records?\nEnter 1 for YES\nEnter 2 for NO\n"))
  if choice_display == 1:
    print("Employee Records")
    print("\n----------------------------------------")
    Management.display_records()

  choice=int(input("\nDo you wish to continue?\nEnter 1 for YES\nEnter 2 for NO\n"))

  if choice == 2:
    print("Thank you")

    break