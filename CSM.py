class Employee:
    no_of_leavs = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name} salary is {self.salary} and role is{self.role}"

    @classmethod
    def change_leaves(cls,newleavs):
        cls.no_of_leavs = newleavs

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        #return "no smoking"


davide = Employee("davide",400,"Instructor")
harry = Employee("harry",500,"student")




print(harry.printgood("harry"))
