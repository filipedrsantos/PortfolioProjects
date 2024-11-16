SELECT *
FROM EmployeeDemographics

Select FirstName, LastName, Age,
Case
	When Age > 30 Then 'Old' --order of the conditions matter
	When Age BETWEEN 27 and 30 Then 'Young'
	Else 'Baby'
End as adjective
From EmployeeDemographics
Where Age is NOT NULL
Order by Age

SELECT *
FROM EmployeeSalary

Select FirstName, LastName, JobTitle, Salary,
Case
	When JobTitle = 'Salesman' Then Salary + (Salary*.10)
	Else Salary + (Salary*.05)
	End As SalaryAfterRase
From EmployeeDemographics
Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID