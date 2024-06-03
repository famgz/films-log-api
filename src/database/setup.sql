CREATE DATABASE films_log;

USE films_log;

-- Criar tabelas
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE film (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    director VARCHAR(100) NOT NULL,
    duration INT NOT NULL
);

CREATE TABLE review (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    film_id INT,
    review TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (film_id) REFERENCES film(id)
);

CREATE TABLE rating (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    film_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 10),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (film_id) REFERENCES film(id)
);

CREATE TABLE watchlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    film_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (film_id) REFERENCES film(id)
);
