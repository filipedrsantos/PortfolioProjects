With CTE_Employee as 
(Select FirstName, LastName, Gender, Salary, 
Count(Gender) Over (Partition By Gender) as TotalGender,
AVG(Salary) Over (Partition by Salary) as AvgSalary
From EmployeeDemographics as dem	
Join EmployeeSalary as sal
on dem.EmployeeID = sal.EmployeeID
Where Salary > '45000')
Select* --We need to put the Select statement right after the CTE
From CTE_Employee