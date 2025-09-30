# Lab 06 – Notes (ATM Class & Package)

## 1) Class Diagram – Tóm tắt
- *ATM*: quản lý trạng thái máy (atmId, location, cashLevel) và các nghiệp vụ chính
- *Card*: lưu cardNo/pinHash/status
- *Account*: số tài khoản + balance, có debit() và credit()
- *Transaction*: log giao dịch (txId, type, amount, time, status)
- Quan hệ: ATM --> Card, ATM --> Transaction, Card --> Account, Account --> Transaction

## 2) Package Diagram – Tóm tắt kiến trúc
- *UI*: ATMUI (màn hình/phím)
- *Controller*: ATMController (điều phối)
- *BankService*: BankSystem (xác thực, checkBalance, debit/credit)
- *Hardware*: CardReader, Keypad, Screen, CashDispenser, ReceiptPrinter
- Luồng: UI → Controller → BankService/Hardware

## 3) Lý do thiết kế nhanh
- Tách *boundary / control / service / hardware* để dễ mở rộng & test
- Giao dịch có log Transaction để khôi phục/lần vết
- PIN không lưu dạng plaintext → dùng pinHash trong Card

## 4) Ảnh đính kèm
- class-atm.png
- package-diagram.png
