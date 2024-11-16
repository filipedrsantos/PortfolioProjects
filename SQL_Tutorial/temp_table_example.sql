Create Table #temp_Employee (
EmployeeID int,
JobTitle varchar(100),
Salary int
)

Select*
From #temp_Employee

Insert into #temp_Employee Values(
'1001', 'HR', '45000')

Select*
From #temp_Employee

Insert into #temp_Employee
Select *
From EmployeeSalary

Select*
From #temp_Employee

-- both work
--DROP TABLE IF EXISTS #temp_Employee2
--Drop Table #temp_Employee2

Create Table #temp_Employee2 (
JobTitle varchar(50),
EmployeesPerJob int,
AvgAge int,
AvgSalary int
)

Select*
From #temp_Employee2

Insert into #temp_Employee2
Select JobTitle, Count(JobTitle), Avg(Age), Avg(Salary)
From EmployeeDemographics as emp
Join EmployeeSalary as sal
On emp.EmployeeID = sal.EmployeeID
group by JobTitle

Select*
From #temp_Employee2

