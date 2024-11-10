class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
    
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated Salary for {self.name}: ${self.salary}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name} department.")
    
    def total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total Salary Expenditure for {self.department_name} Department: ${total_salary}")
    
    def display_employees(self):
        if not self.employees:
            print(f"No employees in {self.department_name} department.")
        else:
            print(f"Employees in {self.department_name} Department:")
            for employee in self.employees:
                employee.display_details()

# Interactive code to add employees to a department and display total expenditure
def main():
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)
    
    while True:
        # Ask for employee details
        name = input("Enter employee name (or 'quit' to stop): ")
        if name.lower() == 'quit':
            break
        employee_id = input(f"Enter employee ID for {name}: ")
        salary = float(input(f"Enter salary for {name}: "))
        
        # Create an Employee object and add it to the department
        employee = Employee(name, employee_id, salary)
        department.add_employee(employee)
    
    # Display employees and total salary expenditure
    department.display_employees()
    department.total_salary_expenditure()

if __name__ == "__main__":
    main()
