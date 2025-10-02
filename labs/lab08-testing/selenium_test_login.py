# labs/lab08-testing/selenium_test_login.py
import os, time, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def make_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    driver.set_window_size(1280, 900)
    return driver

def goto_login(driver):
    # Nếu đã có GitHub Pages cho Lab04, đổi LOGIN_URL cho phù hợp:
    url = os.getenv("LOGIN_URL", "http://localhost:8000/docs/lab04/")
    driver.get(url)
    time.sleep(0.😎

def fill_and_submit(driver, username, password, remember=False):
    # CHÚ Ý: Nếu form của nhóm dùng id/selector khác, sửa 4 dòng dưới cho khớp
    user = driver.find_element(By.CSS_SELECTOR, "#username, input[name='username']")
    pwd  = driver.find_element(By.CSS_SELECTOR, "#password, input[name='password']")
    if remember:
        try:
            driver.find_element(By.CSS_SELECTOR, "#rememberMe, input[type='checkbox']").click()
        except Exception:
            pass
    driver.find_element(By.CSS_SELECTOR, "#loginBtn, button[type='submit']").click()
    # nếu nút submit không tự gửi, thì nhập trước rồi click submit:
    try:
        user.clear(); user.send_keys(username)
        pwd.clear();  pwd.send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "#loginBtn, button[type='submit']").click()
    except Exception:
        pass
    time.sleep(0.😎

def get_message(driver):
    # Sửa selector cho đúng vùng thông báo của form (ví dụ #message)
    try:
        el = driver.find_element(By.CSS_SELECTOR, "#message, .toast, .alert")
        return el.text.strip().lower()
    except Exception:
        return driver.page_source.lower()

@pytest.fixture
def driver():
    d = make_driver()
    try:
        yield d
    finally:
        d.quit()

def test_login_success(driver):
    goto_login(driver)
    fill_and_submit(driver, "admin", "123456", remember=True)
    msg = get_message(driver)
    assert ("success" in msg) or ("đăng nhập thành công" in msg)

def test_login_wrong(driver):
    goto_login(driver)
    fill_and_submit(driver, "admin", "sai_pass")
    msg = get_message(driver)
    assert ("invalid" in msg) or ("sai" in msg) or ("không đúng" in msg)

def test_login_empty(driver):
    goto_login(driver)
    fill_and_submit(driver, "", "")
    msg = get_message(driver)
    assert ("required" in msg) or ("vui lòng" in msg) or ("không được để trống" in msg)
