--Insert into EmployeeDemographics VALUES
--(1011, 'Ryan', 'Howard', 26, 'Male'),
--(NULL, 'Holly', 'Flax', NULL, NULL),
--(1013, 'Darryl', 'Philbin', NULL, 'Male')

--Insert into EmployeeSalary VALUES
--(1010, NULL, 47000),
--(NULL, 'Salesman', 43000)

Select *
From EmployeeDemographics

Select *
From EmployeeSalary

Select *
From EmployeeDemographics
Inner Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select *
From EmployeeDemographics
Full Outer Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select *
From EmployeeDemographics
Left Outer Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select *
From EmployeeDemographics
Right Outer Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select EmployeeDemographics.EmployeeID, FirstName, LastName, Jobtitle, Salary
From EmployeeDemographics
Inner Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select EmployeeSalary.EmployeeID, FirstName, LastName, Jobtitle, Salary
From EmployeeDemographics
Right Outer Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select EmployeeDemographics.EmployeeID, FirstName, LastName, Jobtitle, Salary
From EmployeeDemographics
Right Outer Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select EmployeeDemographics.EmployeeID, FirstName, LastName, Salary
From EmployeeDemographics
Inner Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
Where FirstName <> 'Michael'
Order by Salary Desc

Select JobTitle, Avg(Salary)
From EmployeeDemographics
Inner Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
Where JobTitle = 'Salesman'
Group by Jobtitle
