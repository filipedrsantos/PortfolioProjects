SELECT *
FROM EmployeeDemographics

SELECT DISTINCT(Gender)
FROM EmployeeDemographics

SELECT Gender, Count(Gender)
FROM EmployeeDemographics
Group By Gender

SELECT Gender, Count(Gender)
FROM EmployeeDemographics
Where Age > 31
Group By Gender

SELECT Gender, Age, Count(Gender)
FROM EmployeeDemographics
Group By Gender, Age

SELECT Gender, Age, Count(Gender)
FROM EmployeeDemographics
Where Age > 31
Group By Gender, Age

SELECT Gender, Count(Gender)
FROM EmployeeDemographics
Where Age > 31
Group By Gender, Age

SELECT Gender
FROM EmployeeDemographics
Order By Gender

SELECT Gender, Count(Gender) AS CountGender
FROM EmployeeDemographics
Where Age > 31
Group By Gender
Order By CountGender Desc

SELECT *
FROM EmployeeDemographics
Order By Age Asc, Gender Desc

SELECT *
FROM EmployeeDemographics
Order By 4 Asc, 5 Desc
