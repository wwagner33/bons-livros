-- Create the books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    genre VARCHAR(100),
    rating FLOAT CHECK (rating >= 0 AND rating <= 5),
    ratings_count INT CHECK (ratings_count >= 0),
    description TEXT
);

-- Create the users table (for storing user information)
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- Create the ratings table (for storing user ratings for books)
CREATE TABLE ratings (
    rating_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    book_id INT REFERENCES books(book_id) ON DELETE CASCADE,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    rating_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optional: Create an index on the book title for faster lookups
CREATE INDEX idx_books_title ON books(title);
