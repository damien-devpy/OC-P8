from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login(selenium):
    selenium.get("http://localhost:8000")
    selenium.find_element(By.CSS_SELECTOR, "#connect").click()
    mail = selenium.find_element(By.CSS_SELECTOR, "#id_username")
    mail.send_keys("nouvel.user@mail.com")
    password = selenium.find_element(By.CSS_SELECTOR, "#id_password")
    password.send_keys("random_password", Keys.ENTER)
    message = WebDriverWait(selenium, timeout=10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert")))
    assert "Vous êtes maintenant connecté" in message.text
