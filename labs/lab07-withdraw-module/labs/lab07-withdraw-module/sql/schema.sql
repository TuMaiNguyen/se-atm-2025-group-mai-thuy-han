-- Tạo DB & user (chỉnh lại mật khẩu nếu cần)
CREATE DATABASE IF NOT EXISTS atm_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'atm_user'@'localhost' IDENTIFIED BY 'atm_pass_123';
GRANT ALL PRIVILEGES ON atm_demo.* TO 'atm_user'@'localhost';
FLUSH PRIVILEGES;

USE atm_demo;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
  account_id   INT AUTO_INCREMENT PRIMARY KEY,
  account_no   VARCHAR(20) UNIQUE NOT NULL,
  balance      DECIMAL(14,2) NOT NULL DEFAULT 0
);

CREATE TABLE cards (
  card_no   VARCHAR(32) PRIMARY KEY,
  pin_hash  VARCHAR(64) NOT NULL,
  status    ENUM('ACTIVE','BLOCKED') DEFAULT 'ACTIVE',
  account_id INT NOT NULL,
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE transactions (
  tx_id         INT AUTO_INCREMENT PRIMARY KEY,
  account_id    INT NOT NULL,
  card_no       VARCHAR(32) NOT NULL,
  atm_id        INT NOT NULL,
  tx_type       ENUM('WITHDRAW','DEPOSIT','TRANSFER') NOT NULL,
  amount        DECIMAL(14,2) NOT NULL,
  balance_after DECIMAL(14,2) NOT NULL,
  created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Dữ liệu mẫu
INSERT INTO accounts(account_no, balance) VALUES
 ('ACC001', 5000000.00), ('ACC002', 1500000.00);

-- Thêm thẻ, hash PIN bằng SHA2(…, 256) ngay trong MySQL
INSERT INTO cards(card_no, pin_hash, status, account_id) VALUES
 ('9704123456780001', SHA2('123456',256), 'ACTIVE', 1),
 ('9704123456780002', SHA2('654321',256), 'ACTIVE', 2);
