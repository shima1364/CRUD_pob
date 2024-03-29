from pyodbc import Row
class EmployeeModel_Class():

    def __init__(self, emp_id=None, fname=None, minit=None, lname=None, job_id=None, job_lvl=None, pub_id=None, hire_date=None):
        self.emp_id = emp_id
        self.firstName = fname
        self.minit = minit
        self.lastName = lname
        self.job_id = job_id
        self.job_lvl = job_lvl
        self.pub_id = pub_id
        self.hire_date = hire_date

    def mapForm(self, row: Row):
       self.emp_id = row.emp_id
       self.firstName = row.first_name
       self.minit = row.minit
       self.lastName = row.last_name
       self.job_id = row.job_id
       self.job_lvl = row.job_lvl
       self.pub_id = row.pub_id
       self.hire_date = row.hire_date



# class SpecialEmployeeClass(PersonModel_Class,EmployeeModel_Class):
#     pass

# myPerson = PersonModel_Class('Ali', 'Rahmani', '4435435', '2000-01-01', 'Male')
# myPerson = PersonModel_Class('Ali', 'Rahmani', '4435435', '2000-01-01', 'Male')
# employee = EmployeeModel_Class('Ali', 'Rahmani', '4435435', '2000-01-01', 'Male', '2021-01-01', 'Single')



