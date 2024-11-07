#employee and department management

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    def display_details(self):
        pass
    
    def update_salary(self):
        pass
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
        
    def add_employee(self):
        #add employee to the department, appending to the list
        pass
    
    def total_salary_expenditure(self):
        #based on the size of the employee list in the department
        pass
    def display_employees(self):
        #display all employees
        pass
    
#interactive code to add employees to a department and display total expenditure
    