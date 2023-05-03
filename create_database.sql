CREATE DATABASE IF NOT EXISTS inventorydb;

USE inventorydb;

CREATE TABLE products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    description VARCHAR(255),
    price FLOAT,
    quantity INT,
    color VARCHAR(255),
    serial VARCHAR(255),
    PRIMARY KEY (id)
);

INSERT INTO products (name, description, price, quantity, color, serial) VALUES
  ('Echo Dot', 'This is a popular smart speaker from Amazon that allows you to control your smart home devices, play music, make calls, and more using voice commands.', 49.99, 100, 'Charcoal', 'ABCD1234'),
  ('Fire TV Stick', 'This streaming device lets you access popular streaming services like Netflix, Hulu, and Amazon Prime Video in 4K Ultra HD and HDR quality.', 39.99, 50, 'Black', 'EFGH5678'),
  ('Instant Pot', 'This pressure cooker can cook a variety of dishes quickly and easily, and is versatile enough to replace multiple kitchen appliances.', 79.00, 200, 'Stainless Steel', 'IJKL9012'),
  ('Apple AirPods Pro', 'These wireless earbuds feature active noise cancellation for immersive sound, as well as a transparency mode that lets you hear your surroundings.', 249.00, 75, 'White', 'MNOP3456'),
  ('Fitbit Inspire 2', 'This fitness tracker lets you monitor your activity, sleep, and heart rate, and comes with a free 1-year trial of Fitbit Premium.', 99.95, 150, 'Black', 'QRST7890'),
  ('Crest Whitestrips', 'This teeth whitening kit includes both long-term and quick treatments for a brighter smile.', 44.99, 100, 'White', 'UVWX1234'),
  ('Fujifilm Instax Mini 11', 'This instant camera lets you take and print photos instantly, and features automatic exposure for easy use.', 69.00, 50, 'Lilac Purple', 'YZAB5678'),
  ('LifeStraw Personal Water Filter', 'This water filter lets you drink directly from streams and lakes, making it an essential tool for hiking and camping.', 19.95, 25, 'Blue', 'CDEF9012'),
  ('Anker PowerCore 10000', 'This portable charger can charge your phone multiple times on a single charge, making it ideal for traveling.', 19.99, 300, 'Black', 'GHIJ3456'),
  ('Panasonic ErgoFit In-Ear Earbud Headphones', 'These earbud headphones offer clear sound and a comfortable fit, making them a popular choice for everyday use.', 9.99, 75, 'Black', 'KLMN7890');

