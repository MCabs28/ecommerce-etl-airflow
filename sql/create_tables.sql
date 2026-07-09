-- Drop tables if they already exist
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100) NOT NULL,
    brand VARCHAR(100),
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,

    customer_id INT NOT NULL,

    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    order_status VARCHAR(20) DEFAULT 'Pending',

    total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);



CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,

    order_id INT NOT NULL,

    product_id INT NOT NULL,

    quantity INT NOT NULL CHECK (quantity > 0),

    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price >= 0),

    CONSTRAINT fk_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);