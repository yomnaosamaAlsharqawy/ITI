import psycopg2

con = psycopg2.connect(database='iti', user='yomnaosama', password='123456789',

                       host='localhost', port='5432')

print('Database opened successfully')
cur = con.cursor()
# cur.execute('''CREATE TABLE Emp_py (first_name text, last_name text ,age int,department text, salary int);''')
# con.commit()
list = []


class Employee:
    def __init__(self, f_name, l_name, age, dep, salary):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.department = dep
        self.salary = salary
        list.append(self)
        cur.execute(
            f'insert into Emp_py (first_name , last_name  ,age ,department , salary)values(\'{f_name}\',\'{l_name}\',{age},\'{dep}\' ,{salary});')
        con.commit()

    def transefer(self, new_dep):
        self.department = new_dep
        cur.execute(f'update Emp_py set Department = \'{new_dep}\' where first_name = \'{self.first_name}\';')
        con.commit()

    def fire(self):
        list.remove(self)
        cur.execute(f'delete from Emp_py where first_name = \'{self.first_name}\'AND last_name = \'{self.last_name}\';')
        con.commit()

    def show(self):
        # cur.execute(f'select * from Emp_py where first_name=\'{f_name}\'and last_name =\'{l_name}\';')
        print(
            f'First_name: {self.first_name}\n Last_name: {self.last_name}\n Age: {self.age}\n Department: {self.department}\n Salary: {self.salary}')

    @staticmethod
    def list_employees():
        # print from list
        # for obj in list:
        # print(
        #     f'First_name: {obj.first_name}\n Last_name: {obj.last_name}\n Age: {obj.age}\n Department: {obj.department}\n Salary: {obj.salary}')
        cur.execute(f'select * from Emp_py;')
        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4])
        con.commit()


class Manager(Employee):
    def __init__(self, f_name, l_name, age, dep, salary, managed_dep):
        super().__init__(f_name, l_name, age, dep, salary)
        self.managed_dep = managed_dep

    def show(self):
        print(
            f'First_name: {self.first_name}\n Last_name: {self.last_name}\n Age: {self.age}\n Department: {self.department}\n Salary: confidential\n Mahage_department: {self.managed_dep}')


emp = Employee("yomna", "osama", 23, "AB", 3000)
# Employee.list_employees()
while True:
    option = input(
        'enter (add) for adding new employee \n enter (delete) for delete employee \n enter (update) to update department \n enter (show) to show specific employee \n enter (list) to show all employee\n (q) to exist system:\n')
    if option == "add":
        op = input('enter (m) for adding manager or (e) for adding employee: ')
        if op == "m":
            f_name = input('enter first name:')
            l_name = input('enter last name:')
            age = int(input('enter age:'))
            dep = input('enter department:')
            salary = int(input('enter salary'))
            manage = input('enter managed department')
            emp = Employee(f_name, l_name, age, dep, salary, manage)

        else:
            f_name = input('enter first name:')
            l_name = input('enter last name:')
            age = int(input('enter age:'))
            dep = input('enter department:')
            salary = int(input('enter salary'))
            emp = Employee(f_name, l_name, age, dep, salary)

    elif option == "delete":
        emp.fire()

    elif option == "update":
        new_dep = input('enter new department')
        emp.transefer(new_dep)
    elif option == "show":
        emp.show()

    elif option == "list":
        Employee.list_employees()

    else:
        break
