Select *
From EmployeeDemographics
Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select JobTitle, Count(Jobtitle)
From EmployeeDemographics
Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
Group by Jobtitle
Having Count(JobTitle) > 1

Select JobTitle, AVG(Salary)
From EmployeeDemographics
Join EmployeeSalary
ON EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
Group by Jobtitle
Having AVG(Salary) > 30000 AND Count(JobTitle) > 1
Order by AVG(Salary) Desc