select distinct city from station
where not regexp_like(lower(city), '^[aeiou]') and
not regexp_like(lower(city), '[aeiou]$');
