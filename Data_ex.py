from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_weather(city_name):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://weather.com/")

        # 1) Dismiss privacy/consent banners if they appear
        try:
            consent = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(.,'Accept') or contains(.,'I Agree') or contains(.,'Continue') or contains(.,'Got it')]"
            )))
            consent.click()
        except Exception:
            pass  # No banner or already closed

        # 2) Make sure the search input is present (some layouts need a search-button click first)
        try:
            # If there is a header search button, click it to reveal the input
            btns = driver.find_elements(By.XPATH, "//button[contains(@aria-label,'Search') or contains(@data-testid,'Search')]")
            if btns:
                btns[0].click()
        except Exception:
            pass

        # 3) Find the input robustly (ID may work; otherwise use placeholder/aria-label)
        search_box = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//input[@id='LocationSearch_input' or "
            "contains(@placeholder,'Search City') or contains(@placeholder,'Zip') or "
            "contains(@aria-label,'Search City') or contains(@aria-label,'Zip')]"
        )))
        search_box.clear()
        search_box.send_keys(city_name)

        # 4) Wait for suggestions and pick the first one
        first_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@id='LocationSearch_listbox']//button[1]"
        )))
        first_option.click()

        # 5) Wait for the city page to load and read temp + condition
        temp = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//span[@data-testid='TemperatureValue']"
        ))).text
        cond = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[@data-testid='wxPhrase']"
        ))).text

        print(f"{city_name}: {temp}, {cond}")
    finally:
        # Keep the browser open briefly if you want to see it; otherwise quit immediately
        driver.quit()

# Demo
# get_weather("Los Angeles")
