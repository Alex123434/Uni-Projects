WorkHours = [("Abby", 400), ("Billy", 30), ("Alex", 800)]

def employee_year(WorkHours):

    CurrentMax = 0
    EmployeeYear = ""

    for employee,hours in WorkHours:
        if hours > CurrentMax:
            CurrentMax = hours
            EmployeeYear = employee
        else:
            pass

    return (EmployeeYear,hours)

Result = employee_year(WorkHours)
print(Result)