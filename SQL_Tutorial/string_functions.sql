Drop Table EmployeeErrors;

CREATE TABLE EmployeeErrors (
EmployeeID varchar(50)
,FirstName varchar(50)
,LastName varchar(50)
)

Insert into EmployeeErrors Values 
('1001  ', 'Jimbo', 'Halbert')
,('  1002', 'Pamela', 'Beasely')
,('1005', 'TOby', 'Flenderson - Fired')

Select *
From EmployeeErrors

--Trim

Select EmployeeID, trim(EmployeeID) as IDTRIM
From EmployeeErrors

Select EmployeeID, ltrim(EmployeeID) as IDTRIM
From EmployeeErrors

Select EmployeeID, rtrim(EmployeeID) as IDTRIM
From EmployeeErrors

--Replace

Select LastName, replace(LastName, '- Fired', '') as LastNameFixed
From EmployeeErrors

--Substring

Select SUBSTRING(FirstName,1,3) --start and length
From EmployeeErrors

Select SUBSTRING(FirstName,3,3)
From EmployeeErrors

--Insert into EmployeeDemographics Values
--(1005, 'Toby', 'Flenderson', 32, 'Male')

Select *
From EmployeeErrors

Select *
From EmployeeDemographics

Select err.FirstName, dem.FirstName
From EmployeeErrors as err
Join EmployeeDemographics as dem
on err.FirstName = dem.FirstName

Select err.FirstName, Substring(err.FirstName,1,3), dem.FirstName, Substring(dem.FirstName,1,3)
From EmployeeErrors as err
Join EmployeeDemographics as dem
on Substring(err.FirstName,1,3) = Substring(dem.FirstName,1,3)

Select err.FirstName, dem.FirstName
From EmployeeErrors as err
Join EmployeeDemographics as dem
on Substring(err.FirstName,1,3) = Substring(dem.FirstName,1,3)

--Gender
--LastName
--Age
--Day of birthday

--Upper and Lower

Select FirstName, Upper(FirstName) as UpperFirstName
From EmployeeErrors

Select FirstName, Lower(FirstName) as LowerFirstName
From EmployeeErrors