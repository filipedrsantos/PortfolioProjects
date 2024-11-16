SELECT *
FROM EmployeeDemographics

SELECT *
FROM WareHouseEmployeeDemographics

Select *
From EmployeeDemographics
Full Outer Join WareHouseEmployeeDemographics
ON EmployeeDemographics.EmployeeID = WareHouseEmployeeDemographics.EmployeeID

SELECT *
FROM EmployeeDemographics
UNION
SELECT *
FROM WareHouseEmployeeDemographics

SELECT *
FROM EmployeeDemographics
UNION ALL --include duplicates
SELECT *
FROM WareHouseEmployeeDemographics
Order by EmployeeID

SELECT EmployeeID, FirstName, Age
FROM EmployeeDemographics
UNION
SELECT EmployeeID, JobTitle, Salary
FROM EmployeeSalary
Order by EmployeeID