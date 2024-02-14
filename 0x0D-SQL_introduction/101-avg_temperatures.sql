-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature in descending order
SELECT city, AVG(value) AS average_temp FROM temperatures GROUP BY city ORDER BY average_temp DESC;
