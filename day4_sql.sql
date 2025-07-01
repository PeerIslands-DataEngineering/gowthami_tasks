SELECT * FROM dev.programmers;

-- Find programmers with a salary equal to $15,000
SELECT * FROM programmers WHERE Salary = 15000;

-- Find programmers with a salary not equal to $15,000
SELECT * FROM programmers WHERE Salary <> 15000;

-- Find programmers with a salary less than $15,000
SELECT * FROM programmers WHERE Salary < 15000;

-- Find programmers with a salary greater than $15,000
SELECT * FROM programmers WHERE Salary > 15000;


-- Find programmers with salaries between $14,000 and $16,000
SELECT Programmer_Name, Salary 
FROM programmers 
WHERE Salary BETWEEN 14000 AND 16000;


-- Find programmers who use Python or JavaScript as their primary language
SELECT Programmer_Name, Primary_Language 
FROM programmers 
WHERE Primary_Language IN ('Python', 'JavaScript');

-- Find programmers whose names start with 'B'
SELECT Programmer_Name 
FROM programmers 
WHERE Programmer_Name LIKE '__n%';




-- Find programmers whose names have 'ar' anywhere in their name
SELECT Programmer_Name 
FROM programmers 
WHERE Programmer_Name LIKE '%ar%';

-- If we had programmers with no secondary language (we don't in our data)
SELECT Programmer_Name 
FROM programmers 
WHERE Secondary_Language IS NULL;

-- Find programmers who have a secondary language specified
SELECT Programmer_Name, Secondary_Language 
FROM programmers 
WHERE Secondary_Language IS NOT NULL;


-- Find female programmers with a salary > $15,000
SELECT Programmer_Name, Gender, Salary 
FROM programmers 
WHERE Gender = 'F' AND Salary > 15000;

-- Find programmers who use either Python or JavaScript as their primary language
SELECT Programmer_Name, Primary_Language 
FROM programmers 
WHERE Primary_Language = 'Python' OR Primary_Language = 'JavaScript';

-- Find programmers who do not use Python as their primary language
SELECT Programmer_Name, Primary_Language 
FROM programmers 
WHERE NOT Primary_Language = 'Python';


-- Calculate 10% bonus for each programmer
SELECT Programmer_Name,
 Salary, Salary * 0.1 AS Bonus,
 Salary + (Salary * 0.1) AS Total_Pay
FROM programmers;

-- Calculate profit from each software (revenue - development cost)
SELECT Programmer_Name, Software_Name, 
       Software_Cost * Sold AS Revenue, 
       Development_Cost AS Cost,
       (Software_Cost * Sold) - Development_Cost AS Profit
FROM software;

 -- Sort by salary in ascending order (default)
SELECT Programmer_Name, Salary 
FROM programmers 
ORDER BY Salary;

-- Sort by salary in descending order
SELECT Programmer_Name, Salary 
FROM programmers 
ORDER BY Salary DESC;

-- Sort by multiple columns
SELECT Programmer_Name, Primary_Language, Salary 
FROM programmers 
ORDER BY Primary_Language, Salary DESC;

-- Find programmers with a salary equal to $15,000
SELECT * FROM programmers WHERE Salary = 15000;

-- Find programmers with a salary not equal to $15,000
SELECT * FROM programmers WHERE Salary <> 15000;

-- Find programmers with a salary less than $15,000
SELECT * FROM programmers WHERE Salary < 15000;

-- Find programmers with a salary greater than $15,000
SELECT * FROM programmers WHERE Salary > 15000;


-- Find programmers with salaries between $14,000 and $16,000
SELECT Programmer_Name, Salary 
FROM programmers 
WHERE Salary BETWEEN 14000 AND 16000;


-- Find programmers who use Python or JavaScript as their primary language
SELECT Programmer_Name, Primary_Language 
FROM programmers 
WHERE Primary_Language IN ('Python', 'JavaScript');

-- Find programmers whose names start with 'B'
SELECT Programmer_Name 
FROM programmers 
WHERE Programmer_Name LIKE '__n%';




-- Find programmers whose names have 'ar' anywhere in their name
SELECT Programmer_Name 
FROM programmers 
WHERE Programmer_Name LIKE '%ar%';

-- If we had programmers with no secondary language (we don't in our data)
SELECT Programmer_Name 
FROM programmers 
WHERE Secondary_Language IS NULL;

-- Find programmers who have a secondary language specified
SELECT Programmer_Name, Secondary_Language 
FROM programmers 
WHERE Secondary_Language IS NOT NULL;


-- Find female programmers with a salary > $15,000
SELECT Programmer_Name, Gender, Salary 
FROM programmers 
WHERE Gender = 'F' AND Salary > 15000;

-- Find programmers who use either Python or JavaScript as their primary language
SELECT Programmer_Name, Primary_Language 
FROM programmers 
WHERE Primary_Language = 'Python' OR Primary_Language = 'JavaScript';

-- Find programmers who do not use Python as their primary language
SELECT Programmer_Name, Primary_Language 
FROM programmers 
WHERE NOT Primary_Language = 'Python';


-- Calculate 10% bonus for each programmer
SELECT Programmer_Name,
 Salary, Salary * 0.1 AS Bonus,
 Salary + (Salary * 0.1) AS Total_Pay
FROM programmers;

-- Calculate profit from each software (revenue - development cost)
SELECT Programmer_Name, Software_Name, 
       Software_Cost * Sold AS Revenue, 
       Development_Cost AS Cost,
       (Software_Cost * Sold) - Development_Cost AS Profit
FROM software;



-- Sort by salary in ascending order (default)
SELECT Programmer_Name, Salary 
FROM programmers 
ORDER BY Salary ASC;

-- Sort by salary in descending order
SELECT Programmer_Name, Salary 
FROM programmers 
ORDER BY Salary DESC;

-- Sort by multiple columns
SELECT Programmer_Name, Primary_Language, Salary 
FROM programmers 
ORDER BY Primary_Language, Salary DESC;


-- Return only the top 5 highest-paid programmers
SELECT Programmer_Name, Salary 
FROM programmers 
ORDER BY Salary DESC 
LIMIT 1,2;

-- Skip the first 3 results and return the next 5 (pagination)
SELECT Programmer_Name, Salary 
FROM programmers 
ORDER BY Salary DESC 
LIMIT 3, 5;  -- Skip 3, take 5


-- 

SELECT Programmer_Name,
       Salary,
       IF(Salary > 15000, 'High', 'Standard') AS Salary_Category
FROM programmers;


-- Categorize programmers by their primary language type
SELECT Programmer_Name,
       Primary_Language,
       CASE 
           WHEN Primary_Language IN ('Python', 'R', 'Julia') THEN 'Data Science'
           WHEN Primary_Language IN ('JavaScript', 'Ruby', 'PHP') THEN 'Web Development'
           WHEN Primary_Language IN ('Java', 'C#', 'C++', 'C') THEN 'Systems Programming'
           ELSE 'Other'
       END AS Language_Category
FROM programmers;

SELECT Programmer_Name,
       DOJ,
       CASE 
           WHEN YEAR(DOJ) <= 1980 THEN 'Veteran'
           WHEN YEAR(DOJ) <= 2000 THEN 'Senior'
           WHEN YEAR(DOJ) <= 2010 THEN 'Mid-level'
           ELSE 'Junior'
       END AS Experience_Level
FROM programmers
ORDER BY DOJ;


-- Display "Not specified" if Secondary_Language is NULL
SELECT Programmer_Name,
       Primary_Language,
       IFNULL(Secondary_Language, 'Not specified') AS Secondary_Language
FROM programmers;


SELECT IFNULL(NULL, "Something which is not null") as test01;

SELECT NULLIF("Python", "Python 3") as test02;


SELECT Programmer_Name,
       DOJ,
       DATE_FORMAT(DOJ, '%M %d, %Y') AS Formatted_DOJ
FROM programmers;


SELECT Programmer_Name
FROM programmers
WHERE MONTH(DOB) = 7; 


SELECT Programmer_Name, 
       Salary,
       ROUND(Salary, 1) AS Rounded_Salary
FROM programmers;


select round(10257, -2);





-- Return NULL if a programmer's primary and secondary languages are the same
SELECT Programmer_Name,
       Primary_Language,
       Secondary_Language,
       NULLIF(Primary_Language, Secondary_Language) AS Different_Primary
FROM programmers;




-- Calculate the absolute difference between a programmer's salary and the average salary
SELECT Programmer_Name, 
       Salary,
       (SELECT AVG(Salary) FROM programmers) AS Avg_Salary,
       ABS(Salary - (SELECT AVG(Salary) FROM programmers)) AS Absolute_Difference
FROM programmers
ORDER BY Absolute_Difference;



SELECT   AVG(Salary)
from programmers;


-- Find programmers whose salary is greater than the average salary
SELECT Programmer_Name, Salary
FROM programmers
WHERE Salary > (SELECT AVG(Salary) FROM programmers);


-- Find programmers who have developed software applications
SELECT Programmer_Name
FROM programmers
WHERE Programmer_Name IN (SELECT Programmer_Name FROM software);

-- Find programmers who have studied at MIT and Stanford
SELECT Programmer_Name
FROM studies
WHERE (Institute, Course) IN (SELECT Institute, Course FROM studies WHERE Institute IN ('MIT', 'Stanford'));


 