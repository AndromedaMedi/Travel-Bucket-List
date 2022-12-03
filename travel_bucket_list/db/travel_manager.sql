DROP TABLE cities;
DROP TABLE countries;
DROP TABLE users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    user_id INT NOT NULL REFERENCES users(id),
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id),
    user_id INT NOT NULL REFERENCES users(id),
    visited BOOLEAN
);
