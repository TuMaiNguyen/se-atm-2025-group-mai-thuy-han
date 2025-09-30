**Init Lab 07**


## 2) Cách chạy trên Windows (XAMPP)

*Các bước:*
1. Cài Python nếu chưa có.
2. Cài XAMPP, mở Control Panel → *Start* MySQL.
3. Mở *phpMyAdmin* (nút *Admin* trong XAMPP) → tab *Import* → chọn file labs/lab07-withdraw-module/sql/schema.sql → *Go* để tạo DB atm_demo và dữ liệu mẫu.
4. (Tuỳ chọn) Sao chép labs/lab07-withdraw-module/.env.example thành .env và chỉnh thông số nếu khác mặc định.
5. Mở *CMD/PowerShell* tại thư mục repo, chạy:
```bash

pip install -r labs/lab07-withdraw-module/requirements.txt
python labs/lab07-withdraw-module/run_demo.py

Kỳ vọng kết quả:

=== ATM Withdraw Demo ===
Card: 9704123456780001 | Amount: 200000
Withdraw success, tx_id = ...

Nếu lỗi: kiểm tra MySQL đang chạy, DB/USER đúng, hoặc số dư không đủ.

``` 

## 3) Screenshot kết quả (bằng chứng chạy được)
Sau khi chạy thành công, chụp màn hình terminal, lưu vào:
labs/lab07-withdraw-module/run-success.png

![Run success](assets/run-success.png)
*Yêu cầu:* Python 3.10+, MySQL đang chạy (XAMPP → Start MySQL).


