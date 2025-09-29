# Lab 03 – UML (Use Case & Sequence) – Withdraw Cash

## 1) Quy trình
Chọn quy trình *Withdraw Cash* của ATM.

## 2) Actors & Lifelines
- *Customer*
(actor): người dùng thực hiện giao dịch tại ATM.
- *ATM_UI*
(boundary): màn hình + keypad, hiển thị & nhận nhập liệu.
- *ATM_Controller*
(control): điều phối nghiệp vụ, gọi phần cứng và dịch vụ ngân hàng.
- *BankSystem*
(participant): core banking – xác thực thẻ/PIN, kiểm tra số dư, ghi nợ, rollback.
- *CashDispenser*
(entity): mô-đun nhả tiền mặt.
- *ReceiptPrinter*
(entity): máy in biên lai.

## 3) Thông điệp chính (theo Sequence)
1. cardInserted(cardNo) → kiểm tra thẻ.
2. submitPIN(cardNo, pin) → xác thực PIN.
3. requestWithdraw(cardNo, amount) → yêu cầu rút tiền.
4. checkBalance(cardNo) → lấy số dư; *alt*: thiếu tiền → kết thúc.
5. debit(cardNo, amount) → ghi nợ; trả về txId.
6. dispense(amount) → nhả tiền; *alt*: lỗi khay → rollback(txId).
7. print(txId, amount, balanceAfter) (opt) → in biên lai.
8. showSuccess(txId, balanceAfter) → hiển thị thành công & trả thẻ.

## 4) Hình ảnh đính kèm
- *Use Case*: uc-withdraw-atm.png
- *Sequence*: sq-withdraw-atm.png


