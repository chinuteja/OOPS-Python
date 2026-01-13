class Employee:

    # Constructor to initialize employee details
    def __init__(self, id, designation, salary)-> None:
        self.id = id
        self.designation = designation
        self.salary = salary

    def travel(self,destination):
        print(f"Employee {self.id} is traveling to {destination}")

# Creating an instance (object) of Employee 
sam = Employee(101, "Manager", 75000)
print(sam.id, sam.designation, sam.salary)  # Output: 101 Manager 75000
print()
sam.travel("New York")  # Output: Employee 101 is traveling to New York
   