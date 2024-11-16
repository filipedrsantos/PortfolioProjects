Select*
From EmployeeDemographics

Update EmployeeDemographics
SET EmployeeID = 1012
Where FirstNAme = 'Holly' And LastName = 'Flax'

Update EmployeeDemographics
SET Age = 31, Gender = 'Female'
Where FirstNAme = 'Holly' And LastName = 'Flax'

Select* --Use this before deleting
From EmployeeDemographics
Where EmployeeID = 1005

--Delete From EmployeeDemographics
--Where EmployeeID = 1005
