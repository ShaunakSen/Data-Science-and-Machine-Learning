## SQLZoo Solutions 

### SELECT FROM world: [link](https://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial)


3

```
SELECT name, gdp/population  FROM world
WHERE population >= 200000000
```

4

```
SELECT name, population/1000000  FROM world
WHERE continent='South America'
```

5

```
SELECT name, population  FROM world
WHERE name IN ('France', 'Germany', 'Italy')
```

6

```
SELECT name FROM world
WHERE name LIKE '%United%'
```

7

```
SELECT name, population, area  FROM world
WHERE area > 3000000 or population > 250000000
```

8

```
SELECT name, population, area  FROM world
WHERE (area > 3000000 or population > 250000000) and 
(area < 3000000 or population < 250000000)
```

9

ROUND(f,p) returns f rounded to p decimal places.

The number of decimal places may be negative, this will round to the nearest 10 (when p is -1) or 100 (when p is -2) or 1000 (when p is -3) etc..

```
SELECT name, ROUND(population/1000000, 2), ROUND(gdp/1000000000,2)  FROM world
WHERE continent='South America'
```

10

```
SELECT name, ROUND(gdp/population, -3) FROM world WHERE gdp >= 1000000000000
```

11

```
SELECT name, capital
  FROM world
 WHERE LENGTH(name) = LENGTH(capital)
```

12

```
SELECT name, capital
FROM world
WHERE (LEFT(name, 1) = LEFT(capital, 1)) AND name <> capital
```

13

```
SELECT name
   FROM world
WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%'
AND name LIKE '%o%' AND name LIKE '%u%' AND name NOT LIKE '% %'
```

### SELECT FROM nobel: [link](https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial)

1

```
SELECT yr, subject, winner
  FROM nobel
 WHERE yr = 1950
 ```

 2

 ```
 SELECT winner
  FROM nobel
 WHERE yr = 1962
   AND subject = 'Literature'
```

3

```
SELECT yr, subject
  FROM nobel
 WHERE winner = 'Albert Einstein'
```

4

```
SELECT winner
  FROM nobel
 WHERE yr >= 2000 AND subject = 'Peace'
```

5

```
SELECT yr, subject, winner
FROM nobel
WHERE subject = 'Literature' AND yr >=1980 AND yr<=1989
```

6

```
SELECT * FROM nobel
 WHERE winner IN ('Theodore Roosevelt',
                  'Woodrow Wilson',
                  'Jimmy Carter',
                'Barack Obama'
)
```

7

```
SELECT winner FROM nobel
WHERE winner LIKE 'John %'
```

8

```
SELECT yr, subject, winner 
FROM nobel
WHERE (yr=1980 AND subject='Physics') OR (yr=1984 AND subject='Chemistry')
```

9

```
SELECT yr, subject, winner 
FROM nobel
WHERE (yr=1980 AND subject<>'Chemistry' AND subject<>'Medicine') 
```

10

```
SELECT yr, subject, winner 
FROM nobel
WHERE (yr<1910 AND subject='Medicine')
OR (yr>=2004 AND subject='Literature') 
```

11

```
SELECT * FROM nobel 
WHERE winner = 'PETER GRÜNBERG'
```

12

```
SELECT * FROM nobel 
WHERE winner = 'EUGENE O\'NEILL'
```

13

```
SELECT winner, yr, subject
FROM nobel
WHERE winner LIKE 'Sir %'

ORDER BY yr DESC, subject ASC
```

14

```
SELECT winner, subject
  FROM nobel
 WHERE yr=1984
 ORDER BY subject IN ('Physics','Chemistry'), subject,winner
```

### SELECT within SELECT: [link](https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial)


1

```
SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')
```

2

```
SELECT name FROM world
  WHERE gdp/population >
     (SELECT gdp/population FROM world
      WHERE name='United Kingdom')
AND continent = 'Europe'
```

3

```
SELECT name, continent FROM world

WHERE continent IN (SELECT continent FROM world WHERE name 
IN ('Argentina', 'Australia'))

ORDER BY name
```

4

```
SELECT name, population FROM world 
WHERE population > (SELECT population FROM world WHERE name = 'Canada' ) AND population < (SELECT population FROM world WHERE name = 'Poland' )
```

5

CONCAT allows you to stick two or more strings together.


```
SELECT name, CONCAT(ROUND(population*100/(SELECT population FROM world WHERE name='Germany')), '%') FROM world WHERE continent='Europe'
```

6

We can use the word ALL to allow >= or > or < or <=to act over a list. For example, you can find the largest country in the world, by population with this query:

```
SELECT name FROM world WHERE gdp > (SELECT MAX(gdp) FROM world WHERE continent = 'Europe'
```

```
SELECT name
  FROM world
 WHERE gdp > ALL(SELECT gdp
                           FROM world
                          WHERE gdp>0 AND continent='Europe')

```

NOTE: `gdp>0` is like a NULL condition filter which is necessary for
the query. Else it does not return anything

7

We can refer to values in the outer SELECT within the inner SELECT. We can name the tables so that we can tell the difference between the inner and outer versions.

```
SELECT continent, name, area FROM world x
  WHERE area >= ALL
    (SELECT area FROM world y
        WHERE y.continent=x.continent
          AND area>0)
```

Again take note of the `area>0` condition as a NULL filter

8

```
SELECT continent, name FROM world x WHERE name <= ALL(SELECT name FROM world y WHERE x.continent = y.continent)
```

9

```
SELECT name, continent, population FROM world WHERE continent IN 
(
SELECT continent FROM
/*select only continents*/
(
/*Find the continents where all countries have a population <= 25000000*/
SELECT continent, MAX(population) FROM world GROUP BY continent HAVING MAX(population) <= 25000000
) as X
)
```

10

```
SELECT name, continent FROM world x WHERE population >= ALL (SELECT 3*population FROM world y WHERE x.continent = y.continent AND x.name <> y.name)
```

### SUM and COUNT: [link](https://sqlzoo.net/wiki/SUM_and_COUNT)

3

```
SELECT SUM(gdp) FROM world WHERE continent = 'Africa'
```

4

```
SELECT COUNT(name) FROM world
WHERE area >= 1000000
```

5

```
SELECT SUM(population) FROM world
WHERE NAME IN ('Estonia', 'Latvia', 'Lithuania')
```

6

```
SELECT continent, COUNT(name) FROM world
GROUP BY continent
```

7

```
SELECT continent, COUNT(name) FROM world
WHERE population >= 10000000
GROUP BY continent
```

NOTE:

The following query throws an error

```
SELECT continent, COUNT(name) FROM world

GROUP BY continent

HAVING population >= 10000000
```

`Unknown column 'population' in 'having clause'`

8

```
SELECT continent FROM world
GROUP BY continent
HAVING SUM(population) >= 100000000
```

### The JOIN operation: [link](https://sqlzoo.net/wiki/The_JOIN_operation)

![](https://sqlzoo.net/w/images/c/ce/FootballERD.png)

1

```
SELECT matchid, player FROM goal 
  WHERE teamid='GER'
```

2

```
SELECT id, stadium, team1, team2
  FROM game
WHERE id = 1012
```

3

```
SELECT player, teamid, stadium, mdate
  FROM game JOIN goal ON (game.id=goal.matchid)
WHERE teamid = 'GER'
```

4

```
SELECT team1, team2, player FROM goal 
JOIN game ON goal.matchid = game.id
WHERE player LIKE 'Mario%'
```
5

```
SELECT player, teamid, coach, gtime 
FROM eteam JOIN goal 
ON eteam.id = goal.teamid 
WHERE gtime <= 10
```

6

```
SELECT mdate, teamname FROM game JOIN eteam ON 
game.team1 = eteam.id
WHERE coach = 'Fernando Santos'
```

7

```
SELECT player FROM goal 
JOIN game ON goal.matchid = game.id
WHERE stadium = 'National Stadium, Warsaw'
```

8

```
SELECT DISTINCT player FROM goal
JOIN game 
ON goal.matchid = game.id
WHERE (team2='GER' OR team1='GER') and (teamid <> 'GER')
```

9

```
SELECT teamname, COUNT(*)
FROM goal
JOIN eteam
ON goal.teamid = eteam.id
GROUP BY teamname
```

10

```
SELECT stadium, COUNT(*)
FROM goal
JOIN game 
ON goal.matchid = game.id 
GROUP BY stadium
```

11

```
SELECT matchid, mdate, COUNT(*)
FROM game
JOIN goal
ON game.id = goal.matchid
WHERE team1='POL' OR team2='POL'
GROUP BY matchid, mdate
```

12

```
SELECT matchid, mdate, COUNT(*)
FROM goal
JOIN game 
ON goal.matchid = game.id
WHERE teamid = 'GER'
GROUP BY matchid, mdate
```

13

```
SELECT mdate, team1,
SUM(CASE WHEN team1=teamid THEN 1 ELSE 0 END) AS score1,
team2,
SUM(CASE WHEN team2=teamid THEN 1 ELSE 0 END) AS score2

FROM game
LEFT JOIN goal
ON game.id = goal.matchid
GROUP BY mdate, team1, team2
ORDER BY mdate, matchid, team1, team2
```

NOTE: we needed 2 CASE WHEN as we wanted to create 2 new cols

Also LEFT JOIN as all matches might not have had goals (0 goals)

In that case teamid will be NULL and score1 and score2 will both be 0

See op: 24 June 2012

```
mdate	team1	score1	team2	score2
24 June 2012	ENG	0	ITA	0
```


### More JOIN operations: [link](https://sqlzoo.net/wiki/More_JOIN_operations)


3

```
SELECT id, title, yr
FROM movie
WHERE title LIKE '%Star Trek%'
ORDER BY yr
```

4

```
SELECT id FROM actor WHERE name = 'Glenn Close'
```

5

```
SELECT id FROM movie WHERE title = 'Casablanca'
```


6

```
SELECT name
FROM movie
JOIN casting
ON (movie.id=casting.movieid)
JOIN actor
ON (casting.actorid = actor.id)
WHERE title='Casablanca'
```

7

```
SELECT name
FROM movie
JOIN casting
ON (movie.id=casting.movieid)
JOIN actor
ON (casting.actorid = actor.id)
WHERE title='Alien'
```

8

```
SELECT title
FROM actor
JOIN casting
ON actor.id = casting.actorid
JOIN movie
ON casting.movieid = movie.id
WHERE name = 'Harrison Ford'
```

9

```
SELECT title
FROM actor
JOIN casting
ON actor.id = casting.actorid
JOIN movie
ON casting.movieid = movie.id
WHERE name = 'Harrison Ford' and ord <> 1
```

10

```
SELECT title, name
FROM movie
JOIN casting
ON movie.id = casting.movieid
JOIN actor
ON casting.actorid = actor.id
WHERE yr=1962 and ord = 1
```

11

```
SELECT yr, COUNT(*) AS num_movies
FROM actor
JOIN casting
ON actor.id = casting.actorid
JOIN movie
ON casting.movieid = movie.id
WHERE name = 'Rock Hudson'
GROUP BY yr
HAVING COUNT(*) > 2
```

12

```
SELECT title, name
FROM movie
JOIN casting
ON movie.id = casting.movieid
JOIN actor 
ON casting.actorid = actor.id
WHERE movieid IN 
(
SELECT DISTINCT movieid
FROM actor
JOIN casting
ON actor.id = casting.actorid
JOIN movie
ON movie.id = casting.movieid
WHERE name = 'Julie Andrews'
)
AND ord = 1
```

13

```
SELECT name
FROM actor
JOIN casting
ON actor.id = casting.actorid
WHERE ord = 1
GROUP BY name
HAVING COUNT(*) >= 30
```

14

```
SELECT title, COUNT(*)
FROM movie
JOIN casting
ON movie.id = casting.movieid
WHERE yr=1978
GROUP BY title
ORDER By COUNT(*) DESC, title
```

15

```
SELECT DISTINCT name FROM
(SELECT DISTINCT actorid FROM casting
WHERE movieid
IN
(
SELECT DISTINCT movieid
FROM actor
JOIN casting
ON casting.actorid = actor.id
WHERE name = 'Art Garfunkel'
)
) as X
JOIN actor
ON X.actorid = actor.id

WHERE name <> 'Art Garfunkel'
```

### Using NULL: [link](https://sqlzoo.net/wiki/Using_Null)

1

```
SELECT name FROM teacher
WHERE dept IS NULL
```

2

```
SELECT teacher.name, dept.name
 FROM teacher INNER JOIN dept
           ON (teacher.dept=dept.id)
```

3

```
SELECT teacher.name, dept.name FROM teacher
LEFT JOIN dept
ON teacher.dept = dept.id
```

4

```
SELECT teacher.name, dept.name FROM dept
LEFT JOIN teacher
ON teacher.dept = dept.id
```

5

COALESCE takes any number of arguments and returns the first value that is not null.

```
SELECT name, COALESCE(mobile, '07986 444 2266')
FROM teacher
```

6

```
SELECT teacher.name, COALESCE(dept.name, 'None') FROM teacher
LEFT JOIN dept
ON teacher.dept = dept.id
```

7

```
SELECT COUNT(name), COUNT(mobile)
FROM teacher
```

8

```
SELECT name, SUM(num_staff)
FROM
(
SELECT dept.name,
CASE WHEN teacher.id IS NULL THEN 0
ELSE 1
END AS num_staff
FROM teacher
RIGHT JOIN dept
ON teacher.dept = dept.id
) as X
GROUP BY name
```

9

```
SELECT teacher.name,
CASE  WHEN dept=1 OR dept=2 THEN 'Sci'
ELSE 'Art'
END
FROM teacher
LEFT JOIN dept
ON teacher.dept = dept.id
```

10

```
SELECT teacher.name,
CASE  WHEN dept=1 OR dept=2 THEN 'Sci'
WHEN dept=3 THEN 'Art'
ELSE 'None'
END
FROM teacher
LEFT JOIN dept
ON teacher.dept = dept.id
```







