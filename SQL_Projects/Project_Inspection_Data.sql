--Inspection Data Project

Select*
From CovidDeaths
order by 3,4

-- Select Data that we are going to use

Select Location, date, total_cases, new_cases, total_deaths, new_deaths, population
From CovidDeaths
--Where location = 'germany' --Germany 1st day data is weird
order by 1,2

------------------------------------------------------ Remove the dates before the first covid case -------------------------------------------------------------------

-- First check what you want to delete
--Select*
--From CovidDeaths
--Where total_cases = 0

-- Then delete it
--Delete From CovidDeaths
--Where total_cases = 0

------------------------------------------------------- Total Cases vs Total Deaths -----------------------------------------------------------------------------------

Select Location, date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage --Use NULLIF to avoid "divide by zero" errors
From CovidDeaths
order by 1,2

-- Check cases in Portugal (using where statements)

Select Location, date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage
From CovidDeaths
Where location like '%portugal%'
order by 1,2

Select Location, date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage
From CovidDeaths
Where location = 'portugal'
order by 1,2

------------------------------------ Before proceding lets change the data type of our date column from "DATETIME" to "DATE" -----------------------------------------

-- option 1, direct update

--ALTER TABLE CovidDeaths
--ALTER COLUMN date DATE;

-- option 2, in order to not lose data, add a new column for the date, and then later if one wishes they may delete the original date column 

-- Add new row for the correct date

ALTER TABLE CovidDeaths
ADD correct_date DATE;

-- Update the new date column using the original date column by converting its data type from "DATETIME" to "DATE"

UPDATE CovidDeaths
SET correct_date = CONVERT(DATE, date);

-- If one whishes they may remove the original date column

--ALTER TABLE CovidDeaths
--DROP COLUMN date;


-- Updated table

Select Location, correct_date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage
From CovidDeaths
Where location = 'portugal'
order by 1,2

-- Check the cases in the last day

SELECT TOP 1 Location, correct_date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage
FROM CovidDeaths
Where location = 'portugal' AND total_cases is NOT NULL
ORDER BY correct_date DESC;

------------------------------------------------------- Order DeathPercentage by country ------------------------------------------------------------------------------

-- 1st approach: By hand chose the last date

Select Location, correct_date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage
From CovidDeaths
Where correct_date = '2024-08-04' --Last date
order by 5 DESC

-- 2nd approach: Selecting the last date using the Max function in a subquery (this does not work because the last date for each location is not be the same)

Select Location, correct_date, total_cases, total_deaths, (total_deaths/NULLIF(total_cases,0))*100 as DeathPercentage
From CovidDeaths
Where correct_date = (SELECT MAX(correct_date) FROM CovidDeaths)
order by 5 DESC

-- 3rd approach: Use a CTE to find the last date for each location, using a partition function

--SELECT Location, 
--       correct_date, 
--       total_cases, 
--       total_deaths,
--       ROW_NUMBER() OVER (PARTITION BY Location ORDER BY correct_date DESC) AS rn
--FROM CovidDeaths
--Order by location

WITH LatestData AS (
    SELECT Location, 
           correct_date, 
           total_cases, 
           total_deaths,
           ROW_NUMBER() OVER (PARTITION BY Location ORDER BY correct_date DESC) AS rn
    FROM CovidDeaths
)
SELECT Location, 
       correct_date, 
       total_cases, 
       total_deaths, 
       (total_deaths / NULLIF(total_cases, 0)) * 100 AS DeathPercentage
FROM LatestData
WHERE rn = 1
ORDER BY DeathPercentage DESC;


-- Total cases vs population

Select Location, correct_date, population, total_cases, (total_cases/population)*100 as InfectionPercentage
From CovidDeaths
Where location = 'portugal'
order by 1,2 DESC

-- Country with highest InfectionPercentage

Select Location, population, Max(total_cases) as HighestInfectionCount, Max((total_cases/population)*100) as MaxInfectionPercentage
From CovidDeaths
group by location, population
order by 4 DESC

-- Check a certain country

Select Location, population, Max(total_cases) as HighestInfectionCount, Max((total_cases/population)*100) as MaxInfectionPercentage
From CovidDeaths
Where Location = 'Japan'
group by location, population

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Country with highest TotalDeathCount

Select Location, Max(total_deaths) as TotalDeathCount
From CovidDeaths
group by location
order by 2 DESC

-- Ignore the rows with continents as countries

Select Location, Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where continent is not null --The rows with continents as locations have NULL in the continent column
group by location
order by 2 DESC

-- Continent with highest TotalDeathCount

-- Using the continent column gives as the wrong results (ex: North America has the same values as United Sates)

Select continent, Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where continent is not null
group by continent
order by 2 DESC

-- Use locations instead, and look for the continents in the location column

Select location, Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where continent is null --Continents as locations
group by location
order by 2 DESC

-- Remove th non-Continent fields
Select location, Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where continent is null AND location NOT LIKE '%-%' AND location NOT LIKE '%(%' AND location <> 'World'
group by location
order by 2 DESC

-- Sum of TotalDeathCount for all continents (using subquery)

SELECT SUM(TotalDeathCount) AS TotalDeathSum
FROM (
    SELECT location, MAX(total_deaths) AS TotalDeathCount
    FROM CovidDeaths
    WHERE continent IS NULL 
      AND location NOT LIKE '%-%' 
      AND location NOT LIKE '%(%'
	  AND location <> 'World'
    GROUP BY location
) AS Subquery;

-- Check if the sum of TotalDeathCount for all continents gives the value of TotalDeathCount for the 'World' field (using union)

Select Max(total_deaths) as TotalDeathCount
From CovidDeaths
Where continent is null AND location = 'World'

UNION ALL --'ALL' since we want to compare two values that we expect to be the same

SELECT SUM(TotalDeathCount) AS TotalDeathSum
FROM (
    SELECT location, MAX(total_deaths) AS TotalDeathCount
    FROM CovidDeaths
    WHERE continent IS NULL 
      AND location NOT LIKE '%-%' 
      AND location NOT LIKE '%(%'
	  AND location <> 'World'
    GROUP BY location
) AS Subquery


-- Continent with highest TotalDeathCount
--Select continent, Max(total_deaths) as TotalDeathCount
--From CovidDeaths
--Where continent is not null
--group by continent
--order by 2 DESC

-------------------------------------------------------- Global numbers -----------------------------------------------------------------------------------------------

Select correct_date, SUM(new_cases) as totalcases, SUM(new_deaths) as totaldeaths, (SUM(new_deaths)/NULLIF(SUM(new_cases),0))*100 as DeathPercentage
From CovidDeaths
Where continent is not null
group by correct_date
order by 1,2

-- Total
Select SUM(new_cases) as totalcases, SUM(new_deaths) as totaldeaths, (SUM(new_deaths)/NULLIF(SUM(new_cases),0))*100 as DeathPercentage
From CovidDeaths
Where continent is not null

------------------------------------------------------- Lets include the Vaccinations table ---------------------------------------------------------------------------

-- Again change the date data type
ALTER TABLE CovidVaccinations
ADD correct_date DATE;

UPDATE CovidVaccinations
SET correct_date = CONVERT(DATE, date);

-- Check the join
Select*
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date

--------------------------------------------------------- Total Population vs Vaccinations -----------------------------------------------------------------------

-- Day by day number of vaccinated people

Select dea.continent, dea.location, dea.correct_date, dea.population, vac.new_vaccinations
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
order by 2,3

-- Total number of Vaccinated peple per country

Select dea.location,
Sum(Cast(vac.new_vaccinations as bigint)) 
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
group by dea.location
order by 1

-- Rolling Count of People Vaccinated

-- 1st approach (incorrect)
Select dea.continent, dea.location, dea.correct_date, dea.population, vac.new_vaccinations,
Sum(Cast(vac.new_vaccinations as bigint)) Over (Partition by dea.location) --change new_vaccinations data type to int (actually to bigint since int is not enough)
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
order by 2,3

-- 2nd approach: in the partition need to order by location and date
Select dea.continent, dea.location, dea.correct_date, dea.population, vac.new_vaccinations,
Sum(Convert(bigint,vac.new_vaccinations)) Over (Partition by dea.location order by dea.location, dea.correct_date) --Convert do the same as Cast as
as RollingPeopleVaccinated  
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
order by 2,3

-- To make calculations with the RollingPeopleVaccinated, since it is not a real column, we need to use CTE or Temp Tables

-- CTE

With PopvsVac (contient, location, correct_date, population, new_vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.correct_date, dea.population, vac.new_vaccinations, 
Sum(Convert(bigint,vac.new_vaccinations)) Over (Partition by dea.location order by dea.location, dea.correct_date) as RollingPeopleVaccinated  --Convert do the same as Cast as 
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
--order by 2,3
)
Select*, (RollingPeopleVaccinated/Population)*100
From PopvsVac
order by 2,3

-- Temp Table

Drop Table if EXISTS #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
continent nvarchar(255),
location nvarchar(255),
correct_date date,
population numeric,
new_vaccination numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.correct_date, dea.population, vac.new_vaccinations, 
Sum(Convert(bigint,vac.new_vaccinations)) Over (Partition by dea.location order by dea.location, dea.correct_date) as RollingPeopleVaccinated  --Convert do the same as Cast as 
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
--order by 2,3

Select*, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated
order by 2,3

------------------------------------------------------ Create Views to store data for visualizations ------------------------------------------------------------------

Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.correct_date, dea.population, vac.new_vaccinations, 
Sum(Convert(bigint,vac.new_vaccinations)) Over (Partition by dea.location order by dea.location, dea.correct_date) as RollingPeopleVaccinated  --Convert do the same as Cast as 
From CovidDeaths as dea
Join CovidVaccinations as vac
On dea.location = vac.location
And dea.correct_date = vac.correct_date
where dea.continent is not null
--order by 2,3

Select*
From PercentPopulationVaccinated