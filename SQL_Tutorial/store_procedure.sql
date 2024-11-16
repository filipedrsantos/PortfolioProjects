CREATE PROCEDURE TEST
As
Select *
From EmployeeDemographics

EXEC TEST

Drop Procedure Temp_Employee 

-- Need to run with the select statement
CREATE PROCEDURE Temp_Employee
As
Create Table #temp_employee (
JobTitle varchar(100),
EmployeesPerJob int,
AvgAge int,
AvgSalary int
)

Insert into #temp_Employee
Select JobTitle, Count(JobTitle), Avg(Age), Avg(Salary)
From EmployeeDemographics as emp
Join EmployeeSalary as sal
On emp.EmployeeID = sal.EmployeeID
group by JobTitle

Select*
From #temp_employee

Exec Temp_Employee

Exec Temp_Employee @Jobtitle = 'Salesman'

