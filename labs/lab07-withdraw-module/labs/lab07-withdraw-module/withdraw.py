# labs/lab07-withdraw-module/withdraw.py
import hashlib
from db import get_connection

class ATMError(Exception):
    pass

def verify_pin(card_no: str, pin: str) -> bool:
    """
    Trả True nếu PIN đúng & thẻ ACTIVE, ngược lại False.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT pin_hash, status FROM cards WHERE card_no=%s", (card_no,))
        row = cur.fetchone()
        if not row:
            return False
        pin_hash_db, status = row
        if status != "ACTIVE":
            return False
        pin_hash_input = hashlib.sha256(pin.encode()).hexdigest()
        return pin_hash_db == pin_hash_input
    finally:
        conn.close()

def withdraw(card_no: str, amount: float, atm_id: int = 1) -> int:
    """
    Thực hiện rút tiền trong 1 transaction:
      - khóa dòng số dư bằng SELECT ... FOR UPDATE
      - kiểm tra số dư
      - trừ tiền
      - ghi log vào bảng transactions
    Trả về tx_id nếu thành công; raise ATMError nếu lỗi.
    """
    if amount <= 0:
        raise ATMError("Amount must be positive")

    conn = get_connection()
    try:
        cur = conn.cursor()

        # Bắt đầu transaction
        cur.execute(
            """
            SELECT a.account_id, a.balance
            FROM accounts a
            JOIN cards c ON c.account_id = a.account_id
            WHERE c.card_no=%s
            FOR UPDATE
            """,
            (card_no,),
        )
        row = cur.fetchone()
        if not row:
            raise ATMError("Card not found")
        account_id, balance = row

        if balance < amount:
            raise ATMError("Insufficient funds")

        # Trừ tiền
        cur.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_id=%s",
            (amount, account_id),
        )

        # Lấy số dư mới để log
        cur.execute("SELECT balance FROM accounts WHERE account_id=%s", (account_id,))
        new_balance = cur.fetchone()[0]

        # Ghi transaction
        cur.execute(
            """
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES (%s, %s, %s, 'WITHDRAW', %s, %s)
            """,
            (account_id, card_no, atm_id, amount, new_balance),
        )

        conn.commit()
        return cur.lastrowid
    except Exception as e:
        conn.rollback()
        raise ATMError(str(e))
    finally:
        conn.close()
