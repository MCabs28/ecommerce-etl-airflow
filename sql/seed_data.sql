INSERT INTO customers (first_name, last_name, email, phone, city, country)
VALUES
('Mark', 'Cabael', 'mark@example.com', '09171234567', 'San Pedro', 'Philippines'),
('Juan', 'Dela Cruz', 'juan@example.com', '09181234567', 'Manila', 'Philippines'),
('Maria', 'Santos', 'maria@example.com', '09191234567', 'Cebu', 'Philippines'),
('John', 'Doe', 'john@example.com', '09201234567', 'Davao', 'Philippines'),
('Jane', 'Smith', 'jane@example.com', '09211234567', 'Baguio', 'Philippines');


INSERT INTO products
(product_name, category, price, stock_quantity)
VALUES
('Laptop', 'Electronics', 55000.00, 20),
('Mechanical Keyboard', 'Electronics', 3500.00, 50),
('Wireless Mouse', 'Electronics', 1200.00, 80),
('27-inch Monitor', 'Electronics', 15000.00, 15),
('USB-C Hub', 'Accessories', 1800.00, 60),
('Office Chair', 'Furniture', 8500.00, 10),
('Standing Desk', 'Furniture', 18500.00, 8),
('Webcam HD', 'Electronics', 2500.00, 40);



INSERT INTO orders
(customer_id, order_date, order_status, total_amount)
VALUES
(1, '2026-07-01', 'Delivered', 58500.00),
(2, '2026-07-02', 'Delivered', 4700.00),
(3, '2026-07-03', 'Pending', 15000.00),
(1, '2026-07-05', 'Shipped', 18500.00),
(4, '2026-07-06', 'Cancelled', 2500.00);


INSERT INTO order_items
(order_id, product_id, quantity, unit_price)
VALUES
(1, 1, 1, 55000.00),
(1, 2, 1, 3500.00),

(2, 3, 1, 1200.00),
(2, 2, 1, 3500.00),

(3, 4, 1, 15000.00),

(4, 7, 1, 18500.00),

(5, 8, 1, 2500.00);