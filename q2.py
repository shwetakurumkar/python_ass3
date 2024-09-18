class Employee:
    def _init_(self):
        self.name = ""
        self.emp_id = ""
        self.department = ""
        self.salary = 0.0

    def accept(self):
        self.name = input("Enter employee name: ")
        self.emp_id = input("Enter employee ID: ")
        self.department = input("Enter employee department: ")
        self.salary = float(input("Enter employee salary: "))

    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary:.2f}")

class Manager(Employee):
    def _init_(self):
        super()._init_()
        self.bonus = 0.0

    def accept(self):
        super().accept()
        self.bonus = float(input("Enter manager bonus: "))

    def display(self):
        super().display()
        print(f"Bonus: {self.bonus:.2f}")
        print(f"Total Salary (Salary + Bonus): {self.salary + self.bonus:.2f}")

def find_max_total_salary(managers):
    if not managers:
        print("No managers to compare.")
        return

    max_manager = max(managers, key=lambda mgr: mgr.salary + mgr.bonus)
    print("\nManager with the maximum total salary:")
    max_manager.display()

num_managers = int(input("Enter the number of managers: "))
managers = []

for _ in range(num_managers):
    manager = Manager()
    print("\nEnter details for Manager:")
    manager.accept()
    managers.append(manager)

find_max_total_salary(managers)