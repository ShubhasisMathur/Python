class Employee:
            empCount=0
            def __init__(self,empname,empemail,empage):
                    self.empname=empname
                    self.empemail= empemail
                    self.empage=empage
                    Employee.empCount +=1
            def displayCount(self):
                    print('Total Emp Count is ' + str(Employee.empCount))
            def displayEmpdetails(self):
                    print('Name is ', self.empname,'Email is ',self.empemail, 'Age is ', self.empage)



                    


