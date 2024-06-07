CREATE DATABASE films_log;

USE films_log;

-- Criar tabelas
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL CHECK (username <> ''), 
    email VARCHAR(100) UNIQUE NOT NULL CHECK (email <> ''), 
    password VARCHAR(100) NOT NULL CHECK (password <> '') 
);

CREATE TABLE film (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL CHECK (title <> ''),
    year INT NOT NULL,
    director VARCHAR(100),
    duration INT NOT NULL
);

CREATE TABLE review (
    user_id INT,
    film_id INT,
    review TEXT NOT NULL CHECK (review <> ''),
    PRIMARY KEY (user_id, film_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (film_id) REFERENCES film(id)
);

CREATE TABLE rating (
    user_id INT,
    film_id INT,
    rating DECIMAL(3,1) CHECK (rating BETWEEN 1 AND 10),
    PRIMARY KEY (user_id, film_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (film_id) REFERENCES film(id)
);

CREATE TABLE favorite (
    user_id INT,
    film_id INT,
    favorite BOOLEAN,
    PRIMARY KEY (user_id, film_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (film_id) REFERENCES film(id)
);
