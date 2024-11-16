--Clean Data Project

Select*
From NashvilleHousing

------------------------------------------------------- Change the date data type from datetime to date ---------------------------------------------------------------

--1st approach, direct update (did not work)

--Select SaleDate, Convert(Date, SaleDate)
--From NashvilleHousing

--Update NashvilleHousing
--Set SaleDate = Convert(Date, SaleDate)

--2nd approach, create a new column and populate it with the converted date

ALTER TABLE NashvilleHousing
ADD converted_date DATE;

Update NashvilleHousing
Set converted_date = Convert(Date, SaleDate)

-- Confirm

Select SaleDate, converted_date
From NashvilleHousing

-- Delete original date column

Alter Table NashvilleHousing
Drop Column SaleDate

-------------------------------------------------------- Fill empty Property Address fields ---------------------------------------------------------------------------

Select PropertyAddress
From NashvilleHousing
Where PropertyAddress is NULL --There are some Property Address fields empty

Select*
From NashvilleHousing
Where PropertyAddress is NULL --There are some Property Address fields empty

Select*
From NashvilleHousing
order by ParcelID --There are duplicate ParcelID's, associated with Property Address empty fields
				 
SELECT UniqueID, COUNT(*) AS DuplicateCount --We cant simply eliminate these duplicates because they are associated to different UniqueID
FROM NashvilleHousing
GROUP BY UniqueID
HAVING COUNT(*) > 1

Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress --Then, we join the table with itself, on the duplicates ParcelID with different UniqueID													
From NashvilleHousing as a
Join NashvilleHousing as b
On a.ParcelID = b.ParcelID
and a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is NULL
order by 1

Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress) --And populate the PropertyAddress of one of the
From NashvilleHousing as a																						  -- tables with those equivalent of the other.
Join NashvilleHousing as b
On a.ParcelID = b.ParcelID
and a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is NULL 

Update a
Set PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
From NashvilleHousing as a
Join NashvilleHousing as b
On a.ParcelID = b.ParcelID
and a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is NULL

Select PropertyAddress
From NashvilleHousing
Where PropertyAddress is NULL --Confirm that there are no null camps left

------------------------------------------- Breaking out Address into Individual Columns (Address,City,State) ---------------------------------------------------------

Select PropertyAddress
From NashvilleHousing

Select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress)) as Address --Serch from position 1 until the comma position
From NashvilleHousing

Select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress)) as Address, CHARINDEX(',',PropertyAddress) --Charindex is a number for the position of the comma
From NashvilleHousing

Select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress) -1) as Address -- Add (-1) to "remove" the comma
From NashvilleHousing

Select
SUBSTRING(PropertyAddress, CHARINDEX(',',PropertyAddress) +1, Len(PropertyAddress)) as Address -- The second part goes from after the comma (+1) until the end
From NashvilleHousing

Select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress) -1) as Address, -- Lets see both cases at the same time
SUBSTRING(PropertyAddress, CHARINDEX(',',PropertyAddress) +1, Len(PropertyAddress)) as Address
From NashvilleHousing

--Lets then add 2 new columns for Address, City and State and fill them using the code above

ALTER TABLE NashvilleHousing
ADD PropertySplitAddress nvarchar(255);

Update NashvilleHousing
Set PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',',PropertyAddress) -1)

ALTER TABLE NashvilleHousing
ADD PropertySplitCity nvarchar(255);

Update NashvilleHousing
Set PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',',PropertyAddress) +1, Len(PropertyAddress))

Select*
From NashvilleHousing

------------------------------------------- Breaking out Owner Address Individual Columns (Address,City,State) --------------------------------------------------------

Select OwnerAddress
From NashvilleHousing

--This time (for sake of variation) we use the function Parsename
Select
Parsename(Replace(OwnerAddress,',','.'),1) --Parsename only works on periods, so we first replace commas by periods
From NashvilleHousing

Select
Parsename(Replace(OwnerAddress,',','.'),3),
Parsename(Replace(OwnerAddress,',','.'),2),
Parsename(Replace(OwnerAddress,',','.'),1)
From NashvilleHousing

--Lets then add 3 new columns for Address, City and State and fill them using the code above 

ALTER TABLE NashvilleHousing
ADD OwnerSplitAddress nvarchar(255);

ALTER TABLE NashvilleHousing
ADD OwnerSplitCity nvarchar(255);

ALTER TABLE NashvilleHousing
ADD OwnerSplitState nvarchar(255);

Update NashvilleHousing
Set OwnerSplitAddress = Parsename(Replace(OwnerAddress,',','.'),3)

Update NashvilleHousing
Set OwnerSplitCity = Parsename(Replace(OwnerAddress,',','.'),2)

Update NashvilleHousing
Set OwnerSplitState = Parsename(Replace(OwnerAddress,',','.'),1)

Select*
From NashvilleHousing

---------------------------------------------------------- Sold on Vacant Y and N to Yes and NO -----------------------------------------------------------------------

--Two ways of checking, and couting the distinct fields in a column

--1st
SELECT SoldAsVacant, COUNT(*) AS DuplicateCount
FROM NashvilleHousing
GROUP BY SoldAsVacant
HAVING COUNT(*) > 1
Order By 2

--2nd
Select Distinct(SoldAsVacant), COUNT(SoldAsVacant) 
From NashvilleHousing
GROUP BY SoldAsVacant
Order BY 2

--Change 'Y' and 'N' to 'Yes' and 'No', using Case satatements

Select SoldAsVacant,
Case
	When SoldAsVacant = 'Y' Then 'Yes'
	When SoldAsVacant = 'N' Then 'No'
	Else SoldAsVacant
	End
FROM NashvilleHousing

Update NashvilleHousing
Set SoldAsVacant = Case
	When SoldAsVacant = 'Y' Then 'Yes'
	When SoldAsVacant = 'N' Then 'No'
	Else SoldAsVacant
	End

--Confirm that the update worked

Select Distinct(SoldAsVacant), COUNT(SoldAsVacant) 
From NashvilleHousing
GROUP BY SoldAsVacant
Order BY 2


------------------------------------------------------------------- Remove Duplicates ---------------------------------------------------------------------------------

--Check duplicantes by partition on some fields and using row_number function

Select*,
ROW_NUMBER() Over (
Partition by ParcelID, 
			 PropertyAddress, 
			 SalePrice,
			 SaleDate,
			 LegalReference
			 Order by UniqueID
			 ) as row_num
From NashvilleHousing
Order by ParcelID

--Use a CTE so we can use the a Where statemente in the "fictitional" column row_num

With RowNumCTE As (
Select*,
ROW_NUMBER() Over (
Partition by ParcelID, 
			 PropertyAddress, 
			 SalePrice,
			 SaleDate,
			 LegalReference
			 Order by UniqueID
			 ) as row_num
From NashvilleHousing
)
Select*
From RowNumCTE
Where row_num > 1
order by PropertyAddress

--Finally delete the rows with row_num > 1

With RowNumCTE As (
Select*,
ROW_NUMBER() Over (
Partition by ParcelID, 
			 PropertyAddress, 
			 SalePrice,
			 SaleDate,
			 LegalReference
			 Order by UniqueID
			 ) as row_num
From NashvilleHousing
)
Delete
From RowNumCTE
Where row_num > 1

--------------------------------------------------------------- Delete unused columns ---------------------------------------------------------------------------------

Select OwnerAddress, TaxDistrict, PropertyAddress
From NashvilleHousing

Alter Table NashvilleHousing
Drop Column OwnerAddress, TaxDistrict, PropertyAddress

Select*
From NashvilleHousing
