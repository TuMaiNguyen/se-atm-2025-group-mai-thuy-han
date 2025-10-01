# labs/lab08-testing/conftest.py
import pathlib
import pytest
import importlib.util

# Trỏ tới thư mục 'labs'
LABS_DIR = pathlib.Path(__file__).resolve().parents[1]

def load_module(module_name: str, relative_path: list[str]):
    """Load a module by file path (vì folder lab07 có dấu '-')"""
    mod_path = LABS_DIR.joinpath(*relative_path)
    spec = importlib.util.spec_from_file_location(module_name, str(mod_path))
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod

@pytest.fixture(scope="session")
def withdraw_mod():
    # Nạp withdraw.py & db.py trong lab07
    withdraw = load_module("withdraw", ["lab07-withdraw-module", "withdraw.py"])
    db = load_module("db", ["lab07-withdraw-module", "db.py"])
    withdraw.get_connection = db.get_connection  # đảm bảo dùng chung kết nối
    return withdraw

@pytest.fixture(autouse=True)
def reset_db(withdraw_mod):
    """Reset dữ liệu trước mỗi test (cần chạy schema.sql trước đó)."""
    conn = withdraw_mod.get_connection()
    try:
        cur = conn.cursor()
        # Dọn log và khôi phục số dư mặc định
        cur.execute("DELETE FROM transactions")
        # ACC001 = 5,000,000 ; ACC002 = 1,500,000
        cur.execute("UPDATE accounts SET balance=5000000 WHERE account_no='ACC001'")
        cur.execute("UPDATE accounts SET balance=1500000 WHERE account_no='ACC002'")
        conn.commit()
    finally:
        conn.close()
    yield
