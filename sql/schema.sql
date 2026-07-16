CREATE TABLE weather_data (

    id INT AUTO_INCREMENT PRIMARY KEY,

    city VARCHAR(50) NOT NULL,

    temperature DECIMAL(5,2),

    feels_like DECIMAL(5,2),

    humidity INT,

    pressure INT,

    weather VARCHAR(50),

    description VARCHAR(100),

    wind_speed DECIMAL(5,2),

    latitude DECIMAL(9,6),

    longitude DECIMAL(9,6),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);