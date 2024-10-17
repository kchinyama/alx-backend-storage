-- demo script of creating a table in sql

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country DEFAULT 'US' CHECK (country IN ('US', 'CO', 'TN'))
	);

