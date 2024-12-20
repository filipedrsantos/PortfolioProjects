USE [SQLTutorial]
GO
/****** Object:  StoredProcedure [dbo].[Temp_Employee]    Script Date: 11/6/2024 3:02:07 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[Temp_Employee]
@JobTitle nvarchar(100)
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
Where Jobtitle = @Jobtitle
group by JobTitle

Select*
From #temp_employee