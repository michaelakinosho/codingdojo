USE world;
-- #1 Query runs and gets all the countries that speak Slovene. Query returns the name of the country, language and language percentage. Query arranges the result by language percentage in descending order. 
SELECT country.Name, countrylanguage.Language, countrylanguage.Percentage FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE	countrylanguage.Language = 'Slovene' ORDER BY countrylanguage.Percentage DESC;

-- #2 Query displays the total number of cities for each country. Query returns the name of the country and the total number of cities. Query arranges the result by the number of cities in descending order.
SELECT country.Name, count(city.ID) AS cities FROM country JOIN city ON country.Code = city.CountryCode GROUP BY country.Name
ORDER BY count(city.ID) DESC;

-- #3 Query runs and gets all the cities in Mexico with a population of greater than 500,000. Query arranges the result by population in descending order.
SELECT city.Name, city.Population, '136' AS country_id FROM city JOIN country ON city.CountryCode = country.Code WHERE country.Name = 'Mexico' and city.Population > 500000 ORDER BY city.Population DESC;

-- #4 Query runs and gets all languages in each country with a percentage greater than 89%. Query arranges the result by percentage in descending order.
SELECT country.Name, countrylanguage.Language, countrylanguage.Percentage FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Percentage > 89.0 ORDER BY countrylanguage.Percentage DESC;

-- #5 Query runs and gets all the countries with Surface Area below 501 and Population greater than 100,000.
SELECT country.Name, country.SurfaceArea, country.Population FROM country WHERE country.SurfaceArea < 501 and country.Population > 100000;

-- #6 Query runs and gets countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years.
SELECT country.Name, country.GovernmentForm, country.Capital, country.LifeExpectancy FROM country WHERE country.GovernmentForm = 'Constitutional Monarchy' and country.Capital > 200 and country.LifeExpectancy > 75;

-- #7 Query runs and gets all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000. The query returns the Country Name, City Name, District and Population.
SELECT country.name AS country_name, city.Name AS city_name, city.District, city.Population FROM country JOIN city ON country.Code = city.CountryCode WHERE city.District = 'Buenos Aires' and city.Population > 500000;

-- #8 Query runs and summarizes the number of countries in each region. The query displays the name of the region and the number of countries. Also, the query arranges the result by the number of countries in descending order.
SELECT country.Region, count(country.Code) as countries FROM country GROUP BY country.Region ORDER BY countries DESC;