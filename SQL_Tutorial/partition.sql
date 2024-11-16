Select*
From EmployeeDemographics as dem	
Join EmployeeSalary as sal
on dem.EmployeeID = sal.EmployeeID

Select FirstName, LastName, Gender, Salary, 
Count(Gender) Over (Partition By Gender) as TotalGender
From EmployeeDemographics as dem	
Join EmployeeSalary as sal
on dem.EmployeeID = sal.EmployeeID

Select FirstName, LastName, Gender, Salary, 
Count(Gender)
From EmployeeDemographics as dem	
Join EmployeeSalary as sal
on dem.EmployeeID = sal.EmployeeID
group by FirstName, LastName, Gender, Salary

Select Gender,
Count(Gender)
From EmployeeDemographics as dem	
Join EmployeeSalary as sal
on dem.EmployeeID = sal.EmployeeID
group by Gender

Select FirstName, LastName, Gender, Salary, 
Count(Gender) Over (Partition By Gender) as TotalGender,
AVG(Salary) Over (Partition by Salary) as AvgSalary
From EmployeeDemographics as dem	
Join EmployeeSalary as sal
on dem.EmployeeID = sal.EmployeeID
Where Salary > '45000'