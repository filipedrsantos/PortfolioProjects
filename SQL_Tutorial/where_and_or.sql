SELECT *
FROM EmployeeDemographics

SELECT *
FROM EmployeeDemographics
Where FirstName = 'Jim'

SELECT *
FROM EmployeeDemographics
Where FirstName <> 'Jim'

SELECT *
FROM EmployeeDemographics
Where Age <= 32 AND Gender = 'Male'

SELECT *
FROM EmployeeDemographics
Where Age <= 32 OR Gender = 'Male'

SELECT *
FROM EmployeeDemographics
Where LastName LIKE 'S%' --'S' in the beginning

SELECT *
FROM EmployeeDemographics
Where LastName LIKE '%S%' --'S' anywhere

SELECT *
FROM EmployeeDemographics
Where LastName LIKE 'S%o%'

SELECT *
FROM EmployeeDemographics
Where FirstName is NOT NULL

SELECT *
FROM EmployeeDemographics
Where FirstName IN ('JIm', 'Michael')