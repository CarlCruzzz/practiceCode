from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://techbeamers.com/selenium-practice-test-page/")

driver.fullscreen_window()


#YUNG SAFE CLICK FUNCTION PARA SA BUTTONS NAG-AI AKO KASI DI KO MASOLVE

def safe_click(driver, locator, timeout=10):
    el = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    # Scroll to the middle of the screen so sticky headers don't cover it
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", el
    )
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locator)).click()
    except Exception as e:
        print(f"Normal click failed for {locator}: {type(e).__name__}. Using JS click.")
        driver.execute_script("arguments[0].click();", el)
    return el

try:

    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    username.send_keys("Test User")

    email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    email.send_keys("carlstephen.cruz@myridius.com")

    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password.send_keys("lebronjames123")

    bio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "bio"))
    )
    bio.send_keys(
        "Hi, I am a Carl Cruz Lebron James Steve Nash Enriquez. "
        "I am testing the Selenium automation script."
    )

    country_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    country = Select(country_element)
    country.select_by_visible_text("Japan")

    languages_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "languages"))
    )
    languages = Select(languages_element)
    languages.select_by_visible_text("Spanish")
    languages.select_by_visible_text("Japanese")
    languages.select_by_visible_text("Chinese")

    sports = safe_click(driver, (By.ID, "sports"))

    music = safe_click(driver, (By.ID, "music"))

    male = safe_click(driver, (By.ID, "male"))

    safe_click(driver, (By.ID, "submit-btn"))

    print("Automation completed!")

except Exception as e:

    print("\n========== ERROR ==========")
    print("Error type:", type(e).__name__)
    print("Error:", e)
    print("===========================\n")

input("Press Enter to close browser...")

driver.quit()