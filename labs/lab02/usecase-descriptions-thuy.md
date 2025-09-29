# Use Case Descriptions – Thùy

## 1) Transfer Funds
**Actor:** Customer  
**Preconditions:** Thẻ hợp lệ; đã xác thực PIN; kết nối core banking OK.  
**Postconditions:** Tài khoản nguồn giảm; tài khoản đích tăng; log giao dịch.

**Main Flow:**
1) Chọn **Transfer Funds** → nhập **Account đích** và **Amount**.  
2) Hệ thống kiểm tra: tài khoản đích tồn tại, số dư nguồn đủ, không vượt hạn mức.  
3) Thực hiện ghi nợ nguồn, ghi có đích (**atomic**).  
4) Hiển thị **thành công**, (tuỳ chọn) **Print Receipt**.  
5) Ghi **transaction log**.

**Exceptions / Alternate:**
- Tài khoản đích **không tồn tại/bị khoá** → báo lỗi, hủy thao tác.  
- **Insufficient funds** → báo lỗi, cho nhập số khác.  
- Lỗi kết nối/timeout → **rollback**, thông báo thất bại.

---

## 2) Change PIN
**Actor:** Customer  
**Preconditions:** Đăng nhập bằng **PIN hiện tại** thành công.  
**Postconditions:** Lưu **PIN mới** (mã hoá); ghi log bảo mật.

**Main Flow:**
1) Chọn **Change PIN**.  
2) Nhập **PIN hiện tại**, **PIN mới**, **Confirm PIN mới**.  
3) Kiểm tra hợp lệ (độ dài, không trùng lặp dễ đoán).  
4) Cập nhật PIN mới.  
5) Thông báo **đổi PIN thành công**.

**Exceptions:**
- PIN hiện tại **sai** → cho nhập lại; quá số lần thì **lock**.  
- **PIN mới ≠ confirm** → báo lỗi, yêu cầu nhập lại.  
- Lỗi DB → **không đổi**, giữ nguyên PIN cũ.
