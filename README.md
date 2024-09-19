# DSA
CREATE KEYSPACE demo
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};


USE demo;


CREATE TABLE users (
    id UUID PRIMARY KEY,
    name text,
    age int
);

INSERT INTO users (id, name, age) VALUES (uuid(), 'David', 22);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Eva', 35);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Frank', 40);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Grace', 29);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Henry', 33);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Ivy', 27);
INSERT INTO users (id, name, age) VALUES (uuid(), 'Jack', 31);

SELECT * FROM users;
