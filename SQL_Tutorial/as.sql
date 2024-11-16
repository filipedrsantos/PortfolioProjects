Select FirstName + ' ' + LastName AS FullName
From EmployeeDemographics

Select AVG(Age) As AverageAge
From EmployeeDemographics

Select Demo.EmployeeID
From EmployeeDemographics As Demo
Join EmployeeSalary As Sal
ON Demo.EmployeeID = Sal.EmployeeID