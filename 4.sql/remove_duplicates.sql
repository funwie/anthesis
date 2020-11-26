-- MySQL

DROP TABLE IF EXISTS ExampleTable;

CREATE TABLE ExampleTable (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user VARCHAR(100) NOT NULL,
    site VARCHAR(255) NOT NULL, 
    customer VARCHAR(255) NOT NULL,
    supplier VARCHAR(255) NOT NULL
);

INSERT INTO ExampleTable (user,site,customer,supplier) 
VALUES ('Carine ','West','Anthesis', 'Sup'),
       ('Jean','North','Ycombinator', 'All'),
       ('Peter','East','Google', 'Ablll'),
       ('Janine ','South','Facebook', 'Buss'),
       ('Jonas ','South West','UN', 'Dss'),
       ('Janine ','South','Facebook', 'Buss'),
       ('Susan','East Cost','Lambda', 'Suses'),
       ('Zbyszek ','Uptown','Yahoo', 'sdfdf'),
       ('Roland','Northern','Apple', 'Rosls'),
       ('Julie','Southern','Slack', 'Julia'),
       ('Kwai','Western','Twitter', 'Kwai'),
       ('Kwai','Western','Twitter', 'Kwai'),
       ('Jean','North','Ycombinator', 'All'),
       ('Susan','East Cost','Lambda', 'Suses'),
       ('Roland','Northern','Apple', 'Rosls');



SELECT 
    user, site, customer,supplier, COUNT(supplier)
FROM
    ExampleTable
GROUP BY 
     user, site, customer,supplier
HAVING 
    COUNT(supplier) > 1;

DELETE e1 FROM ExampleTable e1
INNER JOIN ExampleTable e2 
WHERE 
    e1.id > e2.id 
    AND e1.user = e2.user 
    AND e1.site = e2.site
    AND e1.customer = e2.customer
    AND e1.supplier = e2.supplier;
    
SELECT * FROM ExampleTable;