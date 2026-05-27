CREATE DATABASE IF NOT EXISTS ticket_booking;
USE ticket_booking;
drop database ticket_booking;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password_ VARCHAR(20) NOT NULL
);

CREATE TABLE routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    from_ VARCHAR(50) NOT NULL,
    to_ VARCHAR(50) NOT NULL,
    departure TIME NOT NULL,
    arrival TIME NOT NULL,
    base_price DECIMAL(7,2) NOT NULL,
    UNIQUE KEY unique_route (from_, to_)
);

CREATE TABLE bus (
    bus_id INT AUTO_INCREMENT PRIMARY KEY,
    bus_name VARCHAR(50) NOT NULL DEFAULT 'AMBAL TRAVELS',
    dates DATE NOT NULL,
    route_id INT NOT NULL,
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
);

CREATE TABLE passengers (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    name_ VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    route_id INT NOT NULL,
    mobile VARCHAR(10) NOT NULL,
    email VARCHAR(50) NOT NULL,
    FOREIGN KEY (route_id) REFERENCES routes(route_id)
);

CREATE TABLE seat (
    seat_id INT AUTO_INCREMENT PRIMARY KEY,
    bus_id INT NOT NULL,
    seat_no INT NOT NULL,
    price DECIMAL(7,2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    seat_status VARCHAR(50) DEFAULT 'available',
    FOREIGN KEY (bus_id) REFERENCES bus(bus_id),
    UNIQUE KEY unique_bus_seat (bus_id, seat_no)
);

CREATE TABLE booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT NOT NULL,
    bus_id INT NOT NULL,
    seat_no INT NOT NULL,
    name_ VARCHAR(50) NOT NULL,
    pnr VARCHAR(20) NOT NULL UNIQUE,
    ticket_no VARCHAR(20) NOT NULL UNIQUE,
    payment_type VARCHAR(20) NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'success',
    booked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
    FOREIGN KEY (bus_id) REFERENCES bus(bus_id),
    FOREIGN KEY (bus_id, seat_no) REFERENCES seat(bus_id, seat_no)
);

INSERT INTO users(username, password_)
VALUES ('admin', '1234');

INSERT INTO routes(from_, to_, departure, arrival, base_price)
VALUES ('cumbum', 'coimbatore', '12:00:00', '17:00:00', 500.00);

INSERT INTO bus(bus_name, dates, route_id)
VALUES ('AMBAL TRAVELS', '2027-07-12', 1);

SELECT * FROM users;
SELECT * FROM routes;
SELECT * FROM bus;
SELECT * FROM seat;
SELECT * FROM passengers;
SELECT * FROM booking;