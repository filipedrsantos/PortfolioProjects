Select*
From EmployeeSalary

--Subquery in Select

Select EmployeeID, Salary
From EmployeeSalary

Select EmployeeID, Salary, (Select AVG(Salary) From EmployeeSalary) as AllAvgSalary
From EmployeeSalary

-- Partition By

Select EmployeeID, Salary, AVG(Salary) over () as AllAvgSalary
From EmployeeSalary

-- Group By (does not return what we want)

Select EmployeeID, Salary, AVG(Salary) as AllAvgSalary
From EmployeeSalary
Group By EmployeeID, Salary

-- Subquery in From

Select a.EmployeeID, AllAvgSalary
From (Select EmployeeID, Salary, AVG(Salary) over () as AllAvgSalary
	From EmployeeSalary) a

-- Subquery in Where

Select EmployeeID, Jobtitle, Salary
From EmployeeSalary
Where EmployeeID in (
	Select EmployeeID
	From EmployeeDemographics
	Where Age > 30) 