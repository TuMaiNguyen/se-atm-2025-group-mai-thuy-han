# labs/lab07-withdraw-module/run_demo.py
from withdraw import verify_pin, withdraw, ATMError

def main():
    card = "9704123456780001"
    pin = "123456"
    amount = 200000  # 200k

    print("=== ATM Withdraw Demo ===")
    print("Card:", card, "| Amount:", amount)

    if not verify_pin(card, pin):
        print("PIN invalid or card blocked!")
        return

    try:
        tx_id = withdraw(card, amount)
        print("Withdraw success, tx_id =", tx_id)
    except ATMError as e:
        print("Withdraw failed:", e)

if __name__ == "__main__":
    main()
