# labs/lab08-testing/test_withdraw.py
import pytest

def test_verify_pin_ok(withdraw_mod):
    assert withdraw_mod.verify_pin("9704123456780001", "123456") is True

def test_verify_pin_wrong(withdraw_mod):
    assert withdraw_mod.verify_pin("9704123456780001", "999999") is False

def test_withdraw_success(withdraw_mod):
    # đảm bảo số dư đủ (reset fixture đã set 5,000,000)
    tx_id = withdraw_mod.withdraw("9704123456780001", 200000)  # rút 200k
    assert isinstance(tx_id, int) and tx_id > 0

    # kiểm tra balance giảm & có log
    conn = withdraw_mod.get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT a.balance FROM accounts a
            JOIN cards c ON c.account_id=a.account_id
            WHERE c.card_no=%s
        """, ("9704123456780001",))
        new_balance = float(cur.fetchone()[0])
        assert new_balance == 5000000 - 200000

        cur.execute(
            "SELECT COUNT(*) FROM transactions WHERE card_no=%s AND tx_type='WITHDRAW'",
            ("9704123456780001",)
        )
        count = cur.fetchone()[0]
        assert count >= 1
    finally:
        conn.close()

def test_withdraw_insufficient(withdraw_mod):
    # đặt số dư thấp để fail
    conn = withdraw_mod.get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE accounts a 
            JOIN cards c ON c.account_id=a.account_id
            SET a.balance=100000
            WHERE c.card_no=%s
        """, ("9704123456780001",))
        conn.commit()
    finally:
        conn.close()

    with pytest.raises(withdraw_mod.ATMError):
        withdraw_mod.withdraw("9704123456780001", 200000)  # rút 200k nhưng chỉ có 100k
