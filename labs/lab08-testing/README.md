Init Lab 08
## 1) Cài đặt & Chuẩn bị
- MySQL đang chạy (XAMPP → Start MySQL), DB atm_demo đã import từ labs/lab07-withdraw-module/sql/schema.sql.
- Python 3.10+
- Cài dependency:
```bash
pip install -r labs/lab08-testing/requirements.txt
Nguyen
2) Chạy Unit Test (ATM):
pytest labs/lab08-testing/test_withdraw.py -q --html labs/lab08-testing/reports/unit_report.html --self-contained-html
Kỳ vọng: 4 case pass (PIN đúng/sai, rút thành công/không đủ tiền).
3) Chạy Integration Test (Form Login)
Cách A: Dùng GitHub Pages → đặt biến môi trường:
set LOGIN_URL=https://<username>.github.io/<repo>/docs/lab04/
pytest labs/lab08-testing/selenium_test_login.py -q --html labs/lab08-testing/reports/selenium_report.html --self-contained-html

GitHub Pages
Cách B: Chạy local server:
python -m http.server 8000
# tab khác:
pytest labs/lab08-testing/selenium_test_login.py -q --html labs/lab08-testing/reports/selenium_report.html --self-contained-html
