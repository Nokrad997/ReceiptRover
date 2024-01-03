CREATE TABLE IF NOT EXISTS public."Users"
(
    user_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Users_pkey" PRIMARY KEY (user_id),
    CONSTRAINT email UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Users"
    OWNER to root;




CREATE TABLE IF NOT EXISTS public."Transactions"
(
    transaction_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_id integer NOT NULL,
    date timestamp without time zone DEFAULT (CURRENT_TIMESTAMP(0) + '01:00:00'::interval),
    key text COLLATE pg_catalog."default" NOT NULL,
    scan_id integer NOT NULL,
    CONSTRAINT "Transactions_pkey" PRIMARY KEY (transaction_id),
    CONSTRAINT "key_FK" FOREIGN KEY (key)
        REFERENCES public."Receipt" (key) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "scan_id_FK" FOREIGN KEY (scan_id)
        REFERENCES public."OCRScan" (scan_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "user_id_FK" FOREIGN KEY (user_id)
        REFERENCES public."Users" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Transactions"
    OWNER to root;




CREATE TABLE IF NOT EXISTS public."Receipt"
(
    receipt_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    key text COLLATE pg_catalog."default" NOT NULL,
    receipt bytea NOT NULL,
    CONSTRAINT "Receipt_pkey" PRIMARY KEY (receipt_id),
    CONSTRAINT key UNIQUE (key)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Receipt"
    OWNER to root;


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

CREATE TABLE "Transactions" (
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
    FOREIGN KEY (key) REFERENCES "Transactions" (key)
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