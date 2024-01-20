-- Zapytanie ktore u mnie dziala //MS 

-- Zapytanie ktore u mnie dziala //MS 

CREATE TABLE "User" (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE "OCRScan" (
    scan_id SERIAL PRIMARY KEY,
    scanned_image BYTEA
);

CREATE TABLE "Transaction" (
    transactions_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    scan_id INTEGER,
    key TEXT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES "User" (user_id),
    FOREIGN KEY (scan_id) REFERENCES "OCRScan" (scan_id)
);

CREATE TABLE "Receipt" (
    receipt_id SERIAL PRIMARY KEY,
    key TEXT NOT NULL,
    receipt BYTEA,
    FOREIGN KEY (key) REFERENCES "Transaction" (key)
);

INSERT INTO "User" (name, email, password) VALUES
('John Doe', 'johndoe@example.com', 'password123'),
('Jane Smith', 'janesmith@example.com', 'smithpassword'),
('Alice Johnson', 'alicej@example.com', 'alicepass');

INSERT INTO "OCRScan" (scanned_image) VALUES
('\xdeadbeef'),
('\xcafebabe'),
('\xbaddcafe');

INSERT INTO "Transactions" (user_id, date, scan_id, key) VALUES
(1, '2024-01-10', 1, 'TXN123'),
(2, '2024-01-11', 2, 'TXN124'),
(1, '2024-01-12', 3, 'TXN125');

INSERT INTO "Receipt" (key, receipt) VALUES
('TXN123', '\xdeadbeef'),
('TXN124', '\xcafebabe'),
('TXN125', '\xbaddcafe');
