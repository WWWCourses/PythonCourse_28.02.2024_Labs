class Employee:
    """Represents an employee with a name, ID, salary, and department."""
    def __init__(self, name:str, id:int, salary:float, department:str) -> None:
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def __gt__(s,o):
        return s.salary>o.salary

# Create 5 employee objects with different salaries
employees = [
    Employee("Ivan Petrov", 1234567890, 50000, "Engineering"),
    Employee("Maria Ivanova", 9876543210, 165000, "Marketing"),
    Employee("Mihail Georgiev", 2345678901, 48000, "Sales"),
    Employee("Alisa Stoyanova", 3456789012, 52000, "Human Resources"),
    Employee("Bogomil Nikolov", 5678901234, 70000, "Finance"),
]

# TASK print name of the Employee with highest salary

 # --------------------------------- Variant1: -------------------------------- #
def variant1():
    max_salaray = 0.0
    max_employee = None

    for emp in employees:
        if emp.salary > max_salaray:
            max_salaray = emp.salary
            max_employee = emp

    print(max_employee.name)

# -------------------- Variant1: overload '>' for Employee ------------------- #
def variant2():
    max_employee = employees[0]

    for emp in employees:
        if emp > max_employee:
            max_employee = emp

    print(max_employee.name)

# --------------------------- Variant3: With Sorted -------------------------- #
def variant3():
    sorted_employees = sorted(employees, key=lambda emp:emp.salary)
    print(sorted_employees[-1].name)

# --------------- Variant4: filtering with list comprenhensions -------------- #
# def variant4():
#     max_salaray = max( [emp.salary for emp in employees] )
#     max_salaray_employee = [emp for emp in employees if emp.salary==max_salaray][0]
#     print(max_salaray_employee.name)

# variant4()


# --------------------- Variant5: filtering with filter() -------------------- #
def variant5():
    max_salaray = max( [emp.salary for emp in employees] )
    max_salaray_employee = filter(lambda emp:emp.salary==max_salaray, employees)
    print( list(max_salaray_employee)[0].name)


variant5()