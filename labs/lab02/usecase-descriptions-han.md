# Use Case Descriptions – Hân

   ## 1) Deposit Cash
*Actor:* Customer  
*Goal:* Nộp tiền mặt vào tài khoản tại ATM.  
*Preconditions:* Thẻ hợp lệ; PIN đúng; khay nhận tiền hoạt động.  
*Postconditions:* Số dư tài khoản *tăng*; giao dịch được *log*.

*Main Flow*
1. Customer *Insert Card* → nhập *PIN* → *Authenticate* thành công.
2. Chọn *Deposit Cash*.
3. Đưa tiền vào khay/miệng nhận tiền.
4. ATM *đếm & kiểm tra* tờ (mệnh giá, rách, nghi giả).
5. Hiển thị *số tiền nhận* → Customer *Confirm*.
6. Hệ thống *cộng số dư*; (tuỳ chọn) *Print Receipt*.
7. *Log transaction*, trả thẻ, kết thúc.

*Alternate / Exceptions*
- 4a. Phát hiện tờ *rách/giả* → trả lại, báo lỗi.
- 4b. *Kẹt khay* / cảm biến lỗi → hủy giao dịch, hướng dẫn liên hệ.
- 5a. **Amount vượt hạn mức**/ngày → báo lỗi, cho nhập lại.
- 6a. Lỗi kết nối DB → *rollback*, thông báo thất bại.



  ## 2) Maintain ATM
*Actor:* Technician  
*Goal:* Bảo trì ATM (nạp tiền, thay giấy, kiểm tra thiết bị).  
*Preconditions:* Kỹ thuật viên có *quyền bảo trì*, đăng nhập Service Mode.  
*Postconditions:* Trạng thái/nhật ký bảo trì được cập nhật; ATM sẵn sàng phục vụ.

*Main Flow*
1. Technician *đăng nhập chế độ bảo trì*.
2. Xem *dashboard* tình trạng: cash level, lỗi thiết bị.
3. Thực hiện tác vụ: *nạp tiền*, *thay cuộn giấy*, *làm sạch/khởi động lại* thiết bị.
4. Chạy *self-test* nhanh.
5. Ghi *maintenance log* (thời gian, NV, thao tác).
6. Chuyển trạng thái *In Service* và thoát.

*Exceptions*
- 1a. *Sai xác thực* → từ chối truy cập.
- 3a. *Sai lệch tồn quỹ* → yêu cầu kiểm đếm lại/khóa máy.
- 4a. Thiết bị lỗi nặng → đặt *Out of Service*, tạo ticket hỗ trợ.

*Notes / Business Rules*
- Hạn mức nộp tiền theo lần & theo ngày.
- Tờ nghi giả phải tách riêng, không cộng vào số dư.
