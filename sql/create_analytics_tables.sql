-- Drop analytics tables (development only)
DROP TABLE IF EXISTS analytics_order_items;
DROP TABLE IF EXISTS analytics_orders;
DROP TABLE IF EXISTS analytics_products;
DROP TABLE IF EXISTS analytics_customers;

CREATE TABLE analytics_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP
);

CREATE TABLE analytics_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100),
    brand VARCHAR(100),
    price NUMERIC(10,2),
    stock_quantity INT,
    created_at TIMESTAMP
);

CREATE TABLE analytics_orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP,
    order_status VARCHAR(20),
    total_amount NUMERIC(10,2)
);

CREATE TABLE analytics_order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    unit_price NUMERIC(10,2)
);